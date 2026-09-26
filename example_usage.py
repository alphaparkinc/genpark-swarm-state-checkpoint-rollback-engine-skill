import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SwarmStateCheckpointRollbackEngineClient

def main():
    client = SwarmStateCheckpointRollbackEngineClient()
    res = client.checkpoint_or_rollback_swarm()
    print("=== Swarm State Checkpoint Rollback Engine Output ===")
    print(f"Pipeline: {res['pipeline_id']} | Checkpoints Logged: {res['total_checkpoints_logged']}")
    print(f"Rollback Executed: {res['rollback_executed']} -> Target: {res['last_safe_checkpoint_id']}")
    print(f"Reverted Steps: {res['reverted_step_indices']} | Consistent Hash: {res['active_consistent_state_hash']}")
    print(f"Verdict: {res['system_consistency_verdict']} (Ready for Retry: {res['ready_for_retry']})")

if __name__ == '__main__':
    main()
