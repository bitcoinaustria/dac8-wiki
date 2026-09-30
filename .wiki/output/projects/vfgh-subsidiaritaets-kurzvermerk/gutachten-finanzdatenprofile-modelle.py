#!/usr/bin/env python3
"""Deterministic synthetic models; standard library only; JSON to stdout only.

Run with Python 3 (without -O). Decimal quantities are JSON strings, never
binary floats. No input, network access, real identities or file outputs.
These counterexamples are not an empirical study of Austrian systems, a
canonical reporting schema, a leakage-risk estimate or a legal opinion.
"""

import json
from decimal import Decimal, getcontext
from fractions import Fraction


getcontext().prec = 32
D = Decimal


def model_non_identifiable_stock():
    """The same observation can have distinct economically owned stocks."""
    reports_hold, reports_gift, snapshots = [], [], []
    held, gifted = D("0"), D("0")
    for offset in range(10):
        year = 2026 + offset
        report = {
            "subject": "synthetic-u001", "year": year, "asset": "BTC",
            "fiat_purchase_eur": D("60000"), "purchased_units": D("1"),
            "purchase_count": 1, "outgoing_units": D("1"),
            "outgoing_count": 1, "external_outgoing_units": D("1"),
            "external_outgoing_value_eur": D("60000"),
        }
        reports_hold.append(report.copy())
        reports_gift.append(report.copy())
        held += D("1")
        gifted += D("1") - D("1")
        if offset + 1 in (1, 3, 5, 10):
            snapshots.append({"after_years": offset + 1,
                              "hold_btc": held, "gift_btc": gifted,
                              "hold_value_eur": held * D("60000"),
                              "gift_value_eur": gifted * D("60000")})
    assert reports_hold == reports_gift
    assert [s["hold_btc"] for s in snapshots] == list(map(D, (1, 3, 5, 10)))
    assert all(s["gift_btc"] == 0 for s in snapshots)
    return {
        "assumptions": ["Zero initial BTC; constant EUR 60000/BTC; no fees or debt.",
                        "Both worlds withdraw to an initially own external wallet.",
                        "Hold world retains coins; gift world subsequently gives them away.",
                        "The later gift is outside the observed providers; this is not a claim of universal legal non-reportability.",
                        "General outgoing and its external subset overlap, not two transfers.",
                        "No address anchors, outside events or other information are observed."],
        "annual_reports_identical": reports_hold == reports_gift,
        "annual_reports": reports_hold, "snapshots": snapshots,
        "conclusion": "Annual aggregates alone do not uniquely identify economically owned stock; no estimation-error distribution is measured.",
    }


def model_gross_not_wealth():
    """Twenty purchases and resales recycle the same capital."""
    cash, units, buys, sales = D("10000"), D("0"), D("0"), D("0")
    for _ in range(20):
        cash -= D("10000")
        units += D("1")
        buys += D("10000")
        cash += D("10000")
        units -= D("1")
        sales += D("10000")
        assert cash == D("10000") and units == 0
    assert buys == sales == D("200000")
    return {
        "assumptions": ["Fixed EUR 10000/unit, twenty complete round trips, no costs, taxes, debt or price changes."],
        "round_trips": 20, "initial_capital_eur": D("10000"),
        "gross_purchases_eur": buys, "gross_sales_eur": sales,
        "combined_gross_eur": buys + sales, "net_purchases_eur": buys - sales,
        "closing_cash_eur": cash, "closing_asset_units": units,
        "closing_model_wealth_eur": cash,
        "conclusion": "EUR 200000 of purchases (EUR 400000 two-sided turnover) is not EUR 200000 of wealth.",
    }


def model_cross_provider_join():
    """Annual-only linkage is non-identifiable even with matching totals."""
    def events(out_txid, in_txid):
        return [
            {"provider": "synthetic-p1", "direction": "out", "year": 2026,
             "subject": "synthetic-u001", "asset": "BTC", "units": D("1"),
             "eur": D("10000"), "txid": out_txid},
            {"provider": "synthetic-p2", "direction": "in", "year": 2026,
             "subject": "synthetic-u001", "asset": "BTC", "units": D("1"),
             "eur": D("10000"), "txid": in_txid},
        ]

    def annual(rows):
        return [{key: value for key, value in row.items() if key != "txid"}
                for row in rows]

    def join(rows, reliable_txid):
        outgoing, incoming = rows
        common = (outgoing["year"] == incoming["year"]
                  and outgoing["subject"] == incoming["subject"]
                  and outgoing["asset"] == incoming["asset"]
                  and outgoing["units"] == incoming["units"])
        return common and (not reliable_txid
                           or outgoing["txid"] == incoming["txid"])

    linked = events("synthetic-x1", "synthetic-x1")
    separate = events("synthetic-y1", "synthetic-y2")
    assert annual(linked) == annual(separate)
    assert join(linked, True) and not join(separate, True)
    assert join(linked, False) and join(separate, False)
    assert sum(row["eur"] for row in linked) == D("20000")
    return {
        "assumptions": ["Linked world: one same-owner transfer between providers; ownership verified separately.",
                        "Separate world: a gift out and an independent equal gift in, not the same transaction.",
                        "Fixed EUR 10000/BTC; no fees; one relevant incoming and outgoing transaction per provider.",
                        "Reliable TXID, asset and amount identify this simplified transfer, not economic ownership in general.",
                        "Annual totals here are an observation projection, not a full statutory XML schema."],
        "annual_reports_identical": annual(linked) == annual(separate),
        "annual_reports": annual(linked),
        "linked_events": linked, "separate_events": separate,
        "linked_world_wealth_before_eur": D("10000"),
        "linked_world_wealth_after_eur": D("10000"),
        "naive_in_plus_out_eur": D("20000"), "new_wealth_from_transfer_eur": D("0"),
        "reliable_txid_matching": {"linked": join(linked, True), "separate": join(separate, True)},
        "annual_only_matching": {"linked": join(linked, False), "separate_false_join": join(separate, False)},
        "conclusion": "Both endpoints can describe one movement; equal annual totals do not prove the same movement. No real-world false-join rate is estimated.",
    }


def model_rolling_retention():
    """A period-based ten-year clock; not an authority receipt-based clock."""
    def record(report_year):
        return {"report_year": report_year,
                "expiry_at_end_of_year": report_year + 10,
                "delete_from": f"{report_year + 11}-01-01"}

    old, new = record(2026), record(2036)
    old_expiry_before_new = old["expiry_at_end_of_year"]
    assert old_expiry_before_new == 2036
    assert new["expiry_at_end_of_year"] == 2046
    assert old["expiry_at_end_of_year"] == old_expiry_before_new
    return {
        "assumptions": ["Each record has ten years after its calendar reporting period ends.",
                        "At this model's annual boundary, a record is removed on January 1 after expiry; implementation timing is not observed.",
                        "This models the provider period rule only, not authority receipt clocks, AML relationship-end clocks or exceptions."],
        "old_record": old, "new_record": new,
        "old_clock_reset_by_new_record": False,
        "old_record_expired_on_2037_01_01": 2037 > old["expiry_at_end_of_year"],
        "new_record_expired_on_2037_01_01": 2037 > new["expiry_at_end_of_year"],
        "boundary_note": "Clock dates do not establish when a formal report becomes available or how many reports actually coexist.",
    }


def model_access_reach():
    """Compare accessible cells, retaining identical authorised query results."""
    users, years = 10000, tuple(range(2026, 2036))
    fields = tuple(f"synthetic_field_{number}" for number in range(1, 9))
    routine_year, routine_fields = years[-1], fields[:3]
    full = {
        (user, year): {field: D(user * 1000 + year * 10 + index)
                       for index, field in enumerate(fields)}
        for user in range(1, users + 1) for year in years
    }
    routine = {(user, routine_year): {field: row[field] for field in routine_fields}
               for (user, year), row in full.items() if year == routine_year}
    archive = full.copy()

    def query(store, user, year, requested_fields, role):
        if role == "archive-authorised":
            permitted, source = fields, archive
        elif role == "routine":
            permitted, source = routine_fields, store
        else:
            raise PermissionError("Unknown synthetic role")
        if any(field not in permitted for field in requested_fields):
            raise PermissionError("Field outside synthetic role")
        row = source[(user, year)]
        return {field: row[field] for field in requested_fields}

    archive_equal = all(
        query(routine, user, year, fields, "archive-authorised") == row
        for (user, year), row in full.items()
    )
    routine_equal = all(
        query(routine, user, routine_year, routine_fields, "routine")
        == {field: full[(user, routine_year)][field] for field in routine_fields}
        for user in range(1, users + 1)
    )
    try:
        query(routine, 1, years[0], routine_fields, "routine")
    except KeyError:
        historical_denied = True
    else:
        historical_denied = False
    try:
        query(routine, 1, routine_year, fields, "routine")
    except PermissionError:
        extra_fields_denied = True
    else:
        extra_fields_denied = False
    baseline_cells = users * len(years) * len(fields)
    routine_cells = users * len(routine_fields)
    assert baseline_cells == 800000 and routine_cells == 30000
    assert len(archive) * len(fields) == baseline_cells
    assert archive_equal and routine_equal and historical_denied and extra_fields_denied
    return {
        "assumptions": ["10000 synthetic users, ten years, eight abstract scalar fields; all users covered.",
                        "Baseline routinely exposes all cells; alternative routinely exposes latest year and three fields.",
                        "A logically separate archive role can retrieve the complete retained record.",
                        "This in-memory role model is not a security implementation: no real authentication, encryption, approval, audit or backups are modelled.",
                        "Cells are equally weighted only for counting; their sensitivity and inferential value need not be equal.",
                        "Archive queries are already authorised in the model; legal grounds and approval delay are not tested."],
        "users": users, "years": len(years), "fields_per_full_record": len(fields),
        "routine_fields": len(routine_fields), "routine_years": 1,
        "baseline_routinely_accessible_cells": baseline_cells,
        "alternative_routinely_accessible_cells": routine_cells,
        "routine_cell_reduction": baseline_cells - routine_cells,
        "routine_cell_reduction_percent": D("100") * (1 - D(routine_cells) / D(baseline_cells)),
        "baseline_to_routine_ratio_exact": "80/3",
        "complete_archive_cells": baseline_cells,
        "total_alternative_stored_cells_including_routine_copy": baseline_cells + routine_cells,
        "authorised_full_record_queries_checked": len(full),
        "authorised_archive_query_results_equal": archive_equal,
        "routine_current_subset_queries_equal": routine_equal,
        "routine_historical_query_denied": historical_denied,
        "routine_extra_field_query_denied": extra_fields_denied,
        "conclusion": "Routine reach is smaller, not total stored information. Exact authorised retrieval equality proves neither lower leak probability nor equal administrative detection utility.",
    }


def model_rare_event_base_rate():
    """Exact expected counts, not realised counts from an empirical sample."""
    population, positives = D("100000"), D("100")
    sensitivity, false_positive_rate = D("0.99"), D("0.001")
    negatives = population - positives
    true_positives, false_negatives = positives * sensitivity, positives * (1 - sensitivity)
    false_positives = negatives * false_positive_rate
    true_negatives = negatives * (1 - false_positive_rate)
    precision = true_positives / (true_positives + false_positives)
    exact_precision = Fraction(true_positives) / Fraction(true_positives + false_positives)
    exact_false_discovery = 1 - exact_precision
    assert true_positives == D("99") and false_positives == D("99.9")
    assert true_positives + false_negatives + false_positives + true_negatives == population
    assert true_positives / positives == sensitivity
    assert false_positives / negatives == false_positive_rate
    assert exact_precision == Fraction(110, 221)
    assert D("221") * true_positives == D("110") * (true_positives + false_positives)
    return {
        "assumptions": ["Artificial ground-truth binary labels: 100 positive cases among 100000 candidates.",
                        "Assumed sensitivity 99%; assumed false-positive rate 0.1% among true negatives.",
                        "Fractional counts are mathematical expectations, not observed people or realised classifications.",
                        "No tax, blockchain or Austrian classifier performance is measured."],
        "population": population, "ground_truth_positives": positives,
        "ground_truth_negatives": negatives, "prevalence": positives / population,
        "sensitivity": sensitivity, "false_positive_rate": false_positive_rate,
        "expected_true_positives": true_positives, "expected_false_negatives": false_negatives,
        "expected_false_positives": false_positives, "expected_true_negatives": true_negatives,
        "precision_exact_fraction": f"{exact_precision.numerator}/{exact_precision.denominator}",
        "precision_decimal_approximation": precision,
        "precision_percent_approximation": precision * 100,
        "false_discovery_proportion_exact_fraction": f"{exact_false_discovery.numerator}/{exact_false_discovery.denominator}",
        "conclusion": "A 0.1% false-positive rate can accompany only about 49.77% precision at this rare-event base rate; FPR is not false discoveries divided by all alerts.",
    }


def decimal_json(value):
    if isinstance(value, Decimal):
        return format(value, "f")
    raise TypeError(f"Not JSON serialisable: {type(value).__name__}")


def main():
    if not __debug__:
        raise SystemExit("Run without -O so the model assertions remain active.")
    results = {
        "metadata": {"synthetic_only": True, "deterministic": True,
                     "file_outputs": False, "decimal_precision_digits": getcontext().prec,
                     "decimal_encoding": "JSON strings; precision fraction is exact, recurring decimal is rounded",
                     "scope": "Reproducible counterexamples and access-count model, not completed independent empirical opinion"},
        "1_non_identifiable_stock": model_non_identifiable_stock(),
        "2_gross_not_wealth": model_gross_not_wealth(),
        "3_cross_provider_join": model_cross_provider_join(),
        "4_rolling_retention": model_rolling_retention(),
        "5_access_reach": model_access_reach(),
        "6_rare_event_base_rate": model_rare_event_base_rate(),
        "assertions_passed": True,
    }
    print(json.dumps(results, ensure_ascii=False, indent=2, sort_keys=True, default=decimal_json))


if __name__ == "__main__":
    main()
