#!/usr/bin/env python3
"""Calculate one three-year B2B customer-value scenario."""

from __future__ import annotations

import argparse
import json
from decimal import Decimal, ROUND_HALF_UP


ZERO = Decimal("0")
ONE = Decimal("1")


def decimal_value(raw: str) -> Decimal:
    try:
        value = Decimal(raw)
    except Exception as exc:
        raise argparse.ArgumentTypeError(f"invalid number: {raw}") from exc
    if not value.is_finite():
        raise argparse.ArgumentTypeError(f"number must be finite: {raw}")
    return value


def non_negative(raw: str) -> Decimal:
    value = decimal_value(raw)
    if value < ZERO:
        raise argparse.ArgumentTypeError("value must be non-negative")
    return value


def rate(raw: str) -> Decimal:
    value = decimal_value(raw)
    if value < ZERO or value > ONE:
        raise argparse.ArgumentTypeError("rate must be between 0 and 1")
    return value


def money(value: Decimal) -> str:
    return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def number(value: Decimal) -> str:
    return str(value.quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Calculate a three-year B2B revenue LTV scenario."
    )
    parser.add_argument("--valid-leads", required=True, type=non_negative)
    parser.add_argument("--close-rate", required=True, type=rate)
    parser.add_argument("--small-order-value", required=True, type=non_negative)
    parser.add_argument("--year1-repeat-orders", required=True, type=non_negative)
    parser.add_argument("--year1-repeat-order-value", required=True, type=non_negative)
    parser.add_argument("--year2-retention", required=True, type=rate)
    parser.add_argument("--year2-orders", required=True, type=non_negative)
    parser.add_argument("--year2-order-value", required=True, type=non_negative)
    parser.add_argument("--year3-retention", required=True, type=rate)
    parser.add_argument("--year3-orders", required=True, type=non_negative)
    parser.add_argument("--year3-order-value", required=True, type=non_negative)
    parser.add_argument("--currency", default="CNY")
    parser.add_argument("--gross-margin", type=rate)
    return parser


def calculate(args: argparse.Namespace) -> dict[str, object]:
    acquired = args.valid_leads * args.close_rate
    year1_first_orders = acquired * args.small_order_value
    year1_repeat = acquired * args.year1_repeat_orders * args.year1_repeat_order_value
    year1_revenue = year1_first_orders + year1_repeat

    year2_customers = acquired * args.year2_retention
    year2_revenue = year2_customers * args.year2_orders * args.year2_order_value

    year3_customers = year2_customers * args.year3_retention
    year3_revenue = year3_customers * args.year3_orders * args.year3_order_value

    total = year1_revenue + year2_revenue + year3_revenue
    per_customer = total / acquired if acquired > ZERO else ZERO

    result: dict[str, object] = {
        "currency": args.currency,
        "expected_acquired_customers": number(acquired),
        "year1_first_order_revenue": money(year1_first_orders),
        "year1_repeat_revenue": money(year1_repeat),
        "year1_total_revenue": money(year1_revenue),
        "year2_retained_customers": number(year2_customers),
        "year2_revenue": money(year2_revenue),
        "year3_retained_customers": number(year3_customers),
        "year3_revenue": money(year3_revenue),
        "three_year_customer_pool_value": money(total),
        "three_year_average_ltv_per_acquired_customer": money(per_customer),
    }

    if args.gross_margin is not None:
        result["three_year_gross_profit_contribution"] = money(total * args.gross_margin)
        result["gross_margin"] = number(args.gross_margin)

    return result


def main() -> None:
    args = build_parser().parse_args()
    print(json.dumps(calculate(args), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

