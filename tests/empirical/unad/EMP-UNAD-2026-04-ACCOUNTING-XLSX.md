# EMP-UNAD-2026-04 — Accounting XLSX end-to-end

## Status

`EXECUTED`

## Institution / artifact

- Institution: UNAD
- Artifact: native XLSX workbook
- Domain: basic financial accounting
- Redistribution: source workbook not committed; only anonymized findings are retained

## Why this case matters

This is the first real native spreadsheet execution used to validate Academic Colombia's spreadsheet/artifact path. The workbook contains a journal, T-accounts, trial balance and an exported SIIGO detailed voucher.

## Workbook structure inspected

- `PORTADA`
- `PARTICIPANTE`
- `LIBRO DIARIO`
- `CUENTAS T`
- `BALANCE DE COMPROBACIÓN`
- `COMPROBANTE DETALLADO SIIGO`
- auxiliary imported SIIGO sheet

## Executed checks

### Formula integrity

- journal subtotal formulas were inspected;
- T-account references back to journal cells were inspected;
- trial-balance references back to T-account balances were inspected;
- workbook formula-error scan returned no `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` or `#N/A` matches.

### Double-entry integrity

Fourteen journal transaction blocks were checked. Every `SUMAS IGUALES` row had equal debit and credit totals.

### Trial balance

The final trial balance reports:

- Debit total: COP 117,860,000
- Credit total: COP 117,860,000

The exported SIIGO detailed voucher reports the same debit and credit totals.

### Inventory / cost-of-sales reconciliation

Visible workbook values support:

`initial inventory 17,640,000 + purchases 35,200,000 - ending inventory 29,068,000 = cost of sales 23,772,000`

The resulting COP 23,772,000 matches the cost-of-sales balance used in the workbook and SIIGO voucher.

### Visual inspection

The trial balance was rendered and inspected. The table is legible, totals are visible and no obvious clipping or broken layout was observed in the inspected range.

## Findings

### PASS — spreadsheet dependency chain

The workbook demonstrates a real formula-linked accounting chain:

`LIBRO DIARIO → CUENTAS T → BALANCE DE COMPROBACIÓN`

This is stronger evidence than a static spreadsheet screenshot because downstream balances depend on upstream entries.

### PASS — external-system reconciliation

The final spreadsheet totals reconcile with the SIIGO detailed voucher at COP 117,860,000 on both sides.

### MINOR — account-name consistency

The SIIGO export labels code `61350501` as `Comercio al por mayor y al por menor`, while the workbook trial balance uses the same code as `Costo de ventas`. This should be treated as a cross-system naming/label consistency finding, not as an arithmetic failure.

### MINOR — identity/text quality

The SIIGO export contains a spelling variant in the account-holder surname. Public empirical records intentionally omit personal identifiers.

## Skills empirically exercised

- `academic-artifact-validator`
- `academic-critical-review`
- `academic-final-review`
- `academic-workflow-orchestrator`

Supporting evidence also strengthens requirements/template routing for spreadsheet deliverables.

## Skills not claimed by this case

- `academic-statistical-analysis`: not applicable; accounting arithmetic is not inferential statistics.
- `apa7-academic-style`: not a central gate for this workbook.
- `academic-document-repair`: workbook was inspected, not repaired.

## Empirical conclusion

This case promotes native XLSX coverage from `FIXTURE_READY` to `EXECUTED` for a real formula-driven accounting workbook. It does not claim exhaustive spreadsheet coverage across dashboards, pivots, macros or statistical datasets.
