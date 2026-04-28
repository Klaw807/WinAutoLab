import json

from winautolab.browser_forms import load_workflow


def test_load_workflow_reads_expected_fields(tmp_path):
    config_path = tmp_path / "workflow.json"
    config_path.write_text(
        json.dumps(
            {
                "start_url": "https://example.com/login",
                "username": "user",
                "password": "secret",
                "username_selector": "#username",
                "password_selector": "#password",
                "submit_selector": "#submit",
                "post_login_urls": ["https://example.com/form"],
                "actions": [{"type": "click", "selector": "#go"}],
            }
        ),
        encoding="utf-8",
    )

    workflow = load_workflow(config_path)

    assert workflow.start_url == "https://example.com/login"
    assert workflow.post_login_urls == ["https://example.com/form"]
    assert workflow.actions == [{"type": "click", "selector": "#go"}]

