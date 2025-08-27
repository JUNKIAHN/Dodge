import argparse
import os
from typing import Tuple

import matplotlib.pyplot as plt
import seaborn as sns


def format_currency(value: float) -> str:
	"""Return a human-readable currency string without decimals, e.g., $441,500."""
	return f"${value:,.0f}"


def build_chart_values(
	median_home_price_usd: float,
	median_household_income_usd: float,
) -> Tuple[list, list]:
	labels = [
		"Median home price (Jun 2025)",
		"Median household income (2025 est.)",
	]
	values = [median_home_price_usd, median_household_income_usd]
	return labels, values


def make_chart(
	median_home_price_usd: float,
	median_household_income_usd: float,
	output_path: str,
) -> None:
	"""
	Render and save a bar chart comparing median home price vs. median household income.

	Defaults use public estimates for June 2025:
	- Home price: ~441,500 USD (June 2025 national median sale price proxy)
	- Household income: ~83,150 USD (2025 median household income estimate)
	"""

	sns.set_theme(style="whitegrid")
	labels, values = build_chart_values(median_home_price_usd, median_household_income_usd)
	ratio = median_home_price_usd / max(median_household_income_usd, 1e-9)

	fig, ax = plt.subplots(figsize=(8, 5))
	bar_colors = ["#2a9d8f", "#264653"]
	# Use Matplotlib bars for reliable annotation behavior
	x_positions = list(range(len(labels)))
	bars = ax.bar(x_positions, values, color=bar_colors, width=0.55)
	ax.set_xticks(x_positions, labels)
	ax.set_ylabel("USD")
	ax.set_xlabel("")
	ax.set_title("United States: Home Price vs Household Income (June 2025)")

	# Annotate bars with values
	for idx, bar in enumerate(bars):
		height = bar.get_height()
		ax.text(
			bar.get_x() + bar.get_width() / 2.0,
			height,
			format_currency(values[idx]),
			ha="center",
			va="bottom",
			fontsize=10,
			fontweight="bold",
		)

	# Add affordability ratio annotation
	annot_text = f"Price-to-income ratio: {ratio:.2f}x"
	ax.text(
		0.5,
		1.02,
		annot_text,
		transform=ax.transAxes,
		ha="center",
		va="bottom",
		fontsize=11,
		fontweight="bold",
	)

	# Footnote with source notes (adjust if you replace defaults with official series)
	footnote = (
		"Notes: National figures. Home price ~June 2025 median sale price; "
		"income ~2025 median household income estimate."
	)
	ax.text(0.0, -0.18, footnote, transform=ax.transAxes, fontsize=9, color="#555555")

	plt.tight_layout()
	output_dir = os.path.dirname(output_path) or "."
	os.makedirs(output_dir, exist_ok=True)
	plt.savefig(output_path, dpi=200)
	plt.close(fig)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description=(
			"Generate a bar chart comparing U.S. median home price and median household "
			"income as of June 2025."
		)
	)
	parser.add_argument(
		"--home-price",
		type=float,
		default=441_500,
		help="Median home price in USD for June 2025 (default: 441,500)",
	)
	parser.add_argument(
		"--household-income",
		type=float,
		default=83_150,
		help="Median household income in USD for 2025 estimate (default: 83,150)",
	)
	parser.add_argument(
		"--out",
		default="house_price_vs_income_jun2025.png",
		help="Output PNG path (default: house_price_vs_income_jun2025.png)",
	)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	make_chart(args.home_price, args.household_income, args.out)
	print(f"Saved chart to: {args.out}")


if __name__ == "__main__":
	main()

