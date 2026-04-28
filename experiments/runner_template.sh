#!/usr/bin/env bash
set -euo pipefail

EXPERIMENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "${EXPERIMENT_DIR}/../.." && pwd)"
TOOLKIT_DIR="${WORKSPACE_DIR}/toolkit"
CONFIG_DIR="${EXPERIMENT_DIR}/configs"
RESULTS_DIR="${EXPERIMENT_DIR}/results"
LOG_DIR="${EXPERIMENT_DIR}/logs"

if [[ ! -f "${TOOLKIT_DIR}/shell/load.sh" ]]; then
  echo "[ERROR] Toolkit shell loader not found: ${TOOLKIT_DIR}/shell/load.sh" >&2
  exit 1
fi
source "${TOOLKIT_DIR}/shell/load.sh"

# Set this before the first real run.
conda_env=""

# Add your experiment commands below.
# Return: output_dir, which is the result directly output from the run_expeiment
run_experiment(){
  # Example:
  #   local output_dir="${EXPERIMENT_DIR}/tmp_outputs"
  #   mkdir -p "${output_dir}"
  #   # ... write artifacts into "${output_dir}" ...
  :
}

main() {
  local script_name
  script_name="$(basename "${BASH_SOURCE[0]}" .sh)"

  logging_setup "${LOG_DIR}" "${script_name}"
  setup_conda
  run_experiment
  exp_stage_results "${RESULTS_DIR}" "${output_dir}" $sub_experiment_name
}

sub_experiment_name=""
main "$@"
