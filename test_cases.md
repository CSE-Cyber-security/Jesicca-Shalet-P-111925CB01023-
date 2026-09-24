# Test Cases – Cybersecurity Asset Inventory System

| # | Feature | Input | Expected Output |
|---|---------|-------|------------------|
| 1 | Add Asset | Valid asset (ID: A104, Type: Application, Risk: Low, Status: Secure) | Asset added, confirmation message shown, persisted to `assets.json` |
| 2 | Add Asset – Duplicate ID | Asset ID that already exists (e.g. A101) | Program rejects and re-prompts for a unique ID |
| 3 | Add Asset – Invalid Type | Asset Type: "Laptop" (not in allowed list) | Program rejects and re-prompts until a valid type is entered |
| 4 | Add Asset – Invalid Risk Level | Risk Level: "Extreme" | Program rejects and re-prompts until a valid risk level is entered |
| 5 | Search Asset – Found | Asset ID: A102 | Displays full details of Web-Server |
| 6 | Search Asset – Not Found | Asset ID: Z999 | "No asset found with that ID." |
| 7 | Update Asset | Asset ID: A101, change IP Address | IP Address updated, other fields unchanged, saved to file |
| 8 | Update Asset – Not Found | Asset ID: Z999 | "No asset found with that ID." (no update performed) |
| 9 | Delete Asset – Confirmed | Asset ID: A103, confirm "y" | Asset removed from inventory and file |
| 10 | Delete Asset – Cancelled | Asset ID: A103, confirm "n" | Asset retained, "Deletion cancelled." shown |
| 11 | Delete Asset – Not Found | Asset ID: Z999 | "No asset found with that ID." |
| 12 | Display All Assets | (3 sample assets loaded) | Formatted list of all assets plus summary counts (Total, Critical, High, Medium, Vulnerable, etc.) matching the spec's expected output |
| 13 | Display – Empty Inventory | No assets added | "No assets found." with Total Assets: 0 |
| 14 | Persistence | Add an asset, exit program, restart program, Display All Assets | Previously added asset still present (loaded from `data/assets.json`) |
| 15 | Load Sample Data | Choose menu option 6 on empty inventory | Loads the 3 sample assets (A101, A102, A103) from the problem statement |

## How to Run

```bash
cd src
python3 asset_inventory.py
```

Follow the on-screen menu (1–7) to exercise each test case above.
