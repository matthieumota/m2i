import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] - %(levelname)s - %(message)s",
)

has_failure = False

def run_command(name: str, cmd: list):
    global has_failure

    logging.info(f'Running {name}...')

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        if result.returncode == 0:
            logging.info(f'{name} OK ✅')
        else:
            has_failure = True
            logging.error(f'{name} failed ❌')
            logging.error(result.stdout)
            logging.error(result.stderr)
    except Exception as e:
        has_failure = True
        logging.error(f'Error running {name}: {e}')

run_command('pip audit', ['pip-audit'])
run_command('bandit', ['bandit', 'fake_api.py', 'monitor.py'])
# run_command('not work', ['nw'])

if has_failure:
    exit(1)
