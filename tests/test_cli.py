import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

spec = importlib.util.spec_from_file_location("agent_module", ROOT / "agent.py")
agent_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(agent_module)


def test_collect_user_inputs_returns_defaults(monkeypatch):
    responses = iter(["", "", "", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    values = agent_module.collect_user_inputs()

    assert values["context"] == "Follow up on our product demo from last Tuesday."
    assert values["tone"] == "professional and friendly"
    assert values["recipient"] == "Potential Client"
    assert values["sender"] == "Your Name"
