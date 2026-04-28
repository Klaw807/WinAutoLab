import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class BrowserWorkflow:
    start_url: str
    username: str
    password: str
    username_selector: str
    password_selector: str
    submit_selector: str
    post_login_urls: list[str]
    actions: list[dict[str, Any]]


def load_workflow(path: str | Path) -> BrowserWorkflow:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return BrowserWorkflow(
        start_url=data["start_url"],
        username=data["username"],
        password=data["password"],
        username_selector=data["username_selector"],
        password_selector=data["password_selector"],
        submit_selector=data["submit_selector"],
        post_login_urls=list(data.get("post_login_urls", [])),
        actions=list(data.get("actions", [])),
    )


def run_workflow(config_path: str | Path) -> None:
    from selenium import webdriver

    workflow = load_workflow(config_path)
    driver = webdriver.Chrome()
    try:
        driver.get(workflow.start_url)
        driver.execute_script(
            "document.querySelector(arguments[0]).value = arguments[1]",
            workflow.username_selector,
            workflow.username,
        )
        driver.execute_script(
            "document.querySelector(arguments[0]).value = arguments[1]",
            workflow.password_selector,
            workflow.password,
        )
        driver.execute_script(
            "document.querySelector(arguments[0]).click()",
            workflow.submit_selector,
        )

        for url in workflow.post_login_urls:
            driver.get(url)

        for action in workflow.actions:
            action_type = action["type"]
            if action_type == "click":
                driver.execute_script(
                    "document.querySelector(arguments[0]).click()",
                    action["selector"],
                )
            elif action_type == "set_value":
                driver.execute_script(
                    "document.querySelector(arguments[0]).value = arguments[1]",
                    action["selector"],
                    action["value"],
                )
            elif action_type == "script":
                driver.execute_script(action["code"])
            else:
                raise ValueError(f"Unsupported action type: {action_type}")
    finally:
        driver.quit()

