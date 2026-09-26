import json, sys
from client import SwarmStateCheckpointRollbackEngineClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "swarm-state-checkpoint-rollback-engine", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "checkpoint_or_rollback_swarm", "description": "Manages distributed multi-agent state checkpoints and triggers transactional rollbacks upon failure."}]}}
    elif method == "tools/call":
        client = SwarmStateCheckpointRollbackEngineClient()
        res = client.checkpoint_or_rollback_swarm()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = SwarmStateCheckpointRollbackEngineClient()
        print(json.dumps(client.checkpoint_or_rollback_swarm(), indent=2))
