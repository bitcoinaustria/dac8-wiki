"""Offline countermodels, not a parser, node, classifier or ownership oracle.

All identifiers, quantities, ownership worlds and execution outcomes are synthetic.
Only standard library, no file/network access; deterministic JSON on stdout.
"""

import json
import sys
from decimal import Decimal

if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use -O.")

D = Decimal


def utxo_accounting():
    prevouts = {"SYNTH-A:0": D("0.7"), "SYNTH-B:2": D("0.5")}
    observed_tx = {
        "inputs": ["SYNTH-A:0", "SYNTH-B:2"],
        "outputs": [D("0.4"), D("0.7999")],
    }
    input_sum = sum((prevouts[x] for x in observed_tx["inputs"]), D(0))
    fee = input_sum - sum(observed_tx["outputs"], D(0))
    assert input_sum == D("1.2") and fee == D("0.0001")
    try:
        _ = {"SYNTH-A:0": D("0.7")}["SYNTH-B:2"]
    except KeyError:
        missing_prevout_rejected = True
    else:
        missing_prevout_rejected = False
    assert missing_prevout_rejected
    worlds = {
        "single_owner": {"SYNTH-A:0": "person-X", "SYNTH-B:2": "person-X"},
        "collaborative": {"SYNTH-A:0": "person-X", "SYNTH-B:2": "person-Y"},
    }
    assert worlds["single_owner"] != worlds["collaborative"]
    return {
        "assumptions": "Valid synthetic non-coinbase transaction; signatures not simulated. Output ownership unknown.",
        "transaction_projection_identical_in_both_worlds": observed_tx,
        "different_ownership_worlds": worlds,
        "enriched_input_sum_btc": input_sum,
        "fee_btc": fee,
        "missing_prevout_rejected": missing_prevout_rejected,
        "limits": "Does not construct PayJoin, serialize Bitcoin bytes or measure clustering error frequency.",
    }


def flow_allocation():
    inputs = {"flagged": D("0.5"), "other": D("0.5")}
    outputs = [D("0.6"), D("0.3999")]
    fee = D("0.0001")
    assert sum(inputs.values()) == sum(outputs) + fee
    haircut_share = inputs["flagged"] / sum(inputs.values())
    haircut_output_amounts = [v * haircut_share for v in outputs]
    haircut_fee = fee * haircut_share
    assert sum(haircut_output_amounts) + haircut_fee == inputs["flagged"]
    poison_flags = [True for _ in outputs]
    poison_flagged_face_value = sum(outputs)
    assert poison_flagged_face_value > inputs["flagged"]
    return {
        "assumptions": "Input flag is supplied, not inferred; flagged is a label, not a legal status.",
        "outputs_btc": outputs,
        "poison_output_flags": poison_flags,
        "poison_flagged_face_value_btc": poison_flagged_face_value,
        "haircut_flagged_output_amounts_btc": haircut_output_amounts,
        "haircut_flagged_fee_btc": haircut_fee,
        "limits": "Poison flags reachability; haircut allocates value. They do not measure the same endpoint or prove ownership.",
    }


def cluster_edge_propagation():
    # A and B have the same owner; C and D another. B-C is a mistaken edge.
    true_owner = {"A": "X", "B": "X", "C": "Y", "D": "Y"}
    verified_edges = [("A", "B"), ("C", "D")]
    heuristic_edges = verified_edges + [("B", "C")]

    def components(edges):
        groups = [{x} for x in true_owner]
        for a, b in edges:
            merged = set()
            remaining = []
            for group in groups:
                if a in group or b in group:
                    merged |= group
                else:
                    remaining.append(group)
            groups = remaining + [merged]
        return sorted([sorted(g) for g in groups])

    before = components(verified_edges)
    after = components(heuristic_edges)
    corrected = components([e for e in heuristic_edges if e != ("B", "C")])
    assert before == corrected == [["A", "B"], ["C", "D"]]
    assert after == [["A", "B", "C", "D"]]
    false_person_links = [x for x in after[0] if true_owner[x] != "X"]
    assert false_person_links == ["C", "D"]
    return {
        "assumptions": "Four symbolic addresses with stipulated owners; clustering by transitive connected components.",
        "clusters_before": before,
        "clusters_with_wrong_edge": after,
        "false_links_from_anchor_A": false_person_links,
        "clusters_after_edge_retraction_and_recomputation": corrected,
        "limits": "No empirical error rate; correction requires retained edge provenance and recomputation.",
    }


def bridge_claim_accounting():
    locked = D("1")
    representation = D("1")
    naive = locked + representation
    economic_claim = representation
    assert naive == D("2") and economic_claim == D("1")
    return {
        "assumptions": "One fully collateralised, redeemable 1:1 claim, no other claimant or debt; economic valuation assumed equal.",
        "locked_native_units": locked,
        "representation_units": representation,
        "naive_double_count_units": naive,
        "single_economic_claim_units": economic_claim,
        "limits": "Does not prove bridge reserves, redemption safety, price parity or actual beneficial ownership.",
    }


def snapshot_identity():
    snapshots = [
        {"height": 100, "block_hash": "SYNTH-H-A", "balance": D("1")},
        {"height": 100, "block_hash": "SYNTH-H-B", "balance": D("0")},
    ]
    assert snapshots[0]["height"] == snapshots[1]["height"]
    assert snapshots[0]["block_hash"] != snapshots[1]["block_hash"]
    assert snapshots[0]["balance"] != snapshots[1]["balance"]
    return {
        "assumptions": "Two alternative branches at the same height, not two balances in one canonical state.",
        "alternative_snapshots": snapshots,
        "limits": "No consensus/reorg simulation; height alone is not a branch-unique identifier.",
    }


def execution_revert_boundaries():
    initial = D("2")
    attempted_value = D("1")
    gas_used = 30000
    effective_price_wei = 100 * 10**9
    execution_fee = D(gas_used * effective_price_wei) / D(10**18)
    final_balance = initial - execution_fee
    assert execution_fee == D("0.003") and final_balance == D("1.997")
    ordinary = {"sender_nonce": 1, "delegation": None, "authority_nonce": 7}
    delegated = {"sender_nonce": 1, "delegation": "SYNTH-code", "authority_nonce": 8}
    assert ordinary != delegated
    return {
        "assumptions": "Ordinary valid included transaction with top-level execution failure; synthetic gas values, no blob/L2 fees or concurrent effects. The separate EIP-7702 example projects only status, nonce and delegation after a valid authorization; it has no stipulated gas value or final balance and does not share the ordinary case's fee calculation.",
        "attempted_value_eth": attempted_value,
        "persisted_value_to_recipient_eth": D(0),
        "ordinary_execution_fee_eth": execution_fee,
        "ordinary_final_sender_balance_eth": final_balance,
        "ordinary_gas_used": gas_used,
        "receipt_status_both_worlds": 0,
        "ordinary_preprocessing": ordinary,
        "eip7702_preprocessing": delegated,
        "limits": "Arithmetic only for the ordinary case; EIP-7702 code/nonce/status projection only, not equal gas. No EVM execution or validation of signatures/auth tuples. Receipt failure alone does not prove all transaction-level state unchanged.",
    }


def encode(value):
    if isinstance(value, Decimal):
        return format(value, "f")
    raise TypeError(type(value).__name__)


if __name__ == "__main__":
    models = {
        "C1_utxo_accounting_and_ownership": utxo_accounting(),
        "C2_flow_allocation": flow_allocation(),
        "C3_cluster_edge_propagation": cluster_edge_propagation(),
        "C4_bridge_claim_accounting": bridge_claim_accounting(),
        "C5_snapshot_identity": snapshot_identity(),
        "C6_execution_revert_boundaries": execution_revert_boundaries(),
    }
    json.dump(models, sys.stdout, default=encode, ensure_ascii=False, sort_keys=True, indent=2)
    sys.stdout.write("\n")
