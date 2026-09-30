"""Purely synthetic counterexamples; no personal data or empirical error rates.

Run with Python 3. The JSON on stdout reproduces the memorandum's arithmetic.
Report tuples model only the specified transaction categories, not an XML file.
"""

from decimal import Decimal
import json


def counterexamples():
    price = Decimal("60000")
    one = Decimal("1")
    annual_fields = {
        "fiat_acquisition": {"value_eur": str(price), "btc": str(one), "count": 1},
        "outgoing_transfer": {"value_eur": str(price), "btc": str(one), "count": 1},
        # Overlaps with outgoing_transfer, not a separate additional outflow.
        # The statutory external-address aggregate has no separate count field.
        "external_address_aggregate": {"value_eur": str(price), "btc": str(one)},
    }
    trajectories = [
        {
            "periods": years,
            "same_cumulative_acquisitions_btc": str(one * years),
            "person_a_retains_btc": str(one * years),
            "person_b_gifts_btc_and_retains": "0",
        }
        for years in (1, 3, 5, 10)
    ]
    capital = Decimal("10000")
    cycles = 20
    candidates, true_links, true_positive = 100000, 100, 99
    false_alarm_rate = Decimal("0.001")
    expected_false_positive = Decimal(candidates - true_links) * false_alarm_rate
    precision = Decimal(true_positive) / (true_positive + expected_false_positive)
    assert annual_fields["outgoing_transfer"]["btc"] == "1"
    assert "count" not in annual_fields["external_address_aggregate"]
    assert trajectories[-1]["person_a_retains_btc"] == "10"
    assert capital * cycles == Decimal("200000")
    assert expected_false_positive == Decimal("99.900")
    assert Decimal("0.49") < precision < Decimal("0.50")
    return {
        "status": "synthetic illustration, not a measured population result",
        "assumptions": [
            "zero opening balance, no fees, constant illustrative EUR price",
            "one annual purchase and withdrawal in both cases",
            "subsequent holding or gift occurs outside the reporting provider",
            "external-address classification is a provider-knowledge test",
        ],
        "identical_annual_fields_for_a_and_b": annual_fields,
        "different_stock_trajectories": trajectories,
        "capital_reuse": {
            "capital_eur": str(capital),
            "full_buy_sell_cycles": cycles,
            "gross_acquisitions_eur": str(capital * cycles),
            "gross_disposals_eur": str(capital * cycles),
        },
        "base_rate_illustration": {
            "candidates": candidates,
            "true_links": true_links,
            "true_positive": true_positive,
            "sensitivity": "0.99",
            "false_alarm_rate_among_non_links": str(false_alarm_rate),
            "expected_false_positive": str(expected_false_positive),
            "expected_precision": str(precision),
        },
    }


if __name__ == "__main__":
    print(json.dumps(counterexamples(), ensure_ascii=False, indent=2))
