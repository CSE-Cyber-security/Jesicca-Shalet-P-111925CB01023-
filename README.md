# Week 01 – Cybersecurity Asset Inventory System

A command-line Python application that lets a security administrator **add, search, update, delete, and display** an organization's IT assets, classified by asset type, risk level, and security status.

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
│
├── src/
│   └── asset_inventory.py
│
├── data/
│   └── assets.json
│
├── tests/
│   └── test_cases.md
│
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
│
└── README.md
```

## Features

- **Add Asset** – capture Asset ID, Name, Type, IP Address, OS, Owner/Department, Risk Level, and Security Status, with input validation and duplicate-ID checking.
- **Search Asset** – look up an asset by ID and display its full details.
- **Update Asset** – edit any field of an existing asset (press Enter to keep current values).
- **Delete Asset** – remove an asset after confirmation.
- **Display All Assets** – print every asset plus a summary: total assets, counts by risk level, and counts by security status.
- **Load Sample Data** – quickly populate the inventory with the 3 sample assets from the problem statement.
- **Persistence** – all changes are saved to `data/assets.json` so data survives between runs.

## Data Fields

| Field | Description |
|---|---|
| Asset ID | Unique identifier (e.g. A101) |
| Asset Name | Descriptive name |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Network address |
| Operating System | OS name/version |
| Owner/Department | Responsible department |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## How to Run

```bash
cd src
python3 asset_inventory.py
```

You'll see a menu:

```
1. Add Asset
2. Search Asset
3. Update Asset
4. Delete Asset
5. Display All Assets
6. Load Sample Data
7. Exit
```

Enter a number 1–7 to select an action.

## Sample Output

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
-----------------------------------------
Asset ID    : A101
Asset Name  : HR-PC-01
Asset Type  : Workstation
IP Address  : 192.168.1.10
OS          : Windows 11
Department  : HR
Risk Level  : Medium
Status      : Secure
-----------------------------------------
...
Total Assets      : 3
Critical Assets   : 1
High Risk Assets  : 1
Medium Risk Assets: 1
Vulnerable Assets : 1
=========================================
```

## Testing

See [`tests/test_cases.md`](tests/test_cases.md) for the full list of manual test cases covering valid input, invalid input, missing records, and persistence.

## Screenshots

Add screenshots of each operation (add, display, search, update, delete, summary, and validation handling) to the `screenshots/` folder using the filenames shown in the repository structure above.
