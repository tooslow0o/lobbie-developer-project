alias bashrc='echo .bashrc file working as intended'

function venv {
  # Get the name of the current directory/repo/project
  name=$(basename ${PWD})
  echo ""
  echo "Creating venv for ${name}"

  # Set var for where all virtual environments should live
  dir="${HOME}/python/venvs/${name}"

  # Create main virtual environments directory and subdirectories, skip if it exists with -p
  mkdir -p ${dir}
  echo ""
  echo "venv dir is ${dir}"

  # Create the virtual environment in <virtual environment main directory>/<project name>/venv
  python -m venv "${dir}/venv"
  echo ""
  echo "Activating venv from source ${dir}/venv/bin/activate"
  source "${dir}/venv/bin/activate"

  echo ""
  echo "venv activated, updating pip"
  pip install -U pip
}
