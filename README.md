# Israel tourism country-month ETL

Reproducible ETL for official Israeli inbound tourism arrivals by month and source country.

Run everything:

```bash
PYTHONPATH=src python -m israel_tourism_etl.run_all --start 2015-01 --end 2026-05
```

The current source discovery is conservative: months without an automatically verified official country-month file are written explicitly as `missing` in `data/interim/source_manifest.csv`; no row-level values are invented. Add official CBS or Ministry of Tourism workbook URLs to the manifest and rerun `download_sources`, `build_long_dataset`, `validate_dataset`, and `export_outputs`.

Outputs:
- `data/interim/source_manifest.csv`
- `data/interim/country_normalization_map.csv`
- `data/processed/israel_tourism_country_month_long.csv`
- `outputs/israel_tourism_country_month_long.csv`
- `outputs/israel_tourism_country_month_wide.csv`
- `outputs/validation_report.md`
- `outputs/data_dictionary.md`
