"""
Cybersecurity Asset Inventory System
-------------------------------------
Add, search, update, delete, and display an organization's IT assets.
Data is persisted to ../data/assets.json between runs.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def load_assets():
    """Load the asset list from the JSON data file, if it exists."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_assets(assets):
    """Persist the current asset list to the JSON data file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=4)


# ---------------------------------------------------------------------------
# Input helpers / validation
# ---------------------------------------------------------------------------

def prompt_choice(label, choices):
    """Prompt until the user enters one of the allowed choices (case-insensitive)."""
    choice_str = "/".join(choices)
    while True:
        value = input(f"{label} ({choice_str}): ").strip()
        for c in choices:
            if value.lower() == c.lower():
                return c
        print(f"  Invalid input. Please choose one of: {choice_str}")


def prompt_nonempty(label):
    """Prompt until the user enters a non-empty string."""
    while True:
        value = input(f"{label}: ").strip()
        if value:
            return value
        print("  This field cannot be empty.")


def asset_id_exists(assets, asset_id):
    return any(a["Asset ID"].lower() == asset_id.lower() for a in assets)


# ---------------------------------------------------------------------------
# Core operations
# ---------------------------------------------------------------------------

def add_asset(assets):
    print("\n--- Add New Asset ---")
    while True:
        asset_id = prompt_nonempty("Asset ID")
        if asset_id_exists(assets, asset_id):
            print("  An asset with this ID already exists. Try a different ID.")
        else:
            break

    asset = {
        "Asset ID": asset_id,
        "Asset Name": prompt_nonempty("Asset Name"),
        "Asset Type": prompt_choice("Asset Type", ASSET_TYPES),
        "IP Address": prompt_nonempty("IP Address"),
        "Operating System": prompt_nonempty("Operating System"),
        "Owner/Department": prompt_nonempty("Owner/Department"),
        "Risk Level": prompt_choice("Risk Level", RISK_LEVELS),
        "Security Status": prompt_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"  Asset '{asset_id}' added successfully.")


def search_asset(assets):
    print("\n--- Search Asset ---")
    asset_id = prompt_nonempty("Enter Asset ID to search")
    for a in assets:
        if a["Asset ID"].lower() == asset_id.lower():
            print_asset(a)
            return a
    print("  No asset found with that ID.")
    return None


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset = search_asset(assets)
    if not asset:
        return

    print("Leave a field blank to keep its current value.")
    name = input(f"Asset Name [{asset['Asset Name']}]: ").strip()
    if name:
        asset["Asset Name"] = name

    ip = input(f"IP Address [{asset['IP Address']}]: ").strip()
    if ip:
        asset["IP Address"] = ip

    os_ = input(f"Operating System [{asset['Operating System']}]: ").strip()
    if os_:
        asset["Operating System"] = os_

    dept = input(f"Owner/Department [{asset['Owner/Department']}]: ").strip()
    if dept:
        asset["Owner/Department"] = dept

    change_type = input("Update Asset Type? (y/n): ").strip().lower()
    if change_type == "y":
        asset["Asset Type"] = prompt_choice("Asset Type", ASSET_TYPES)

    change_risk = input("Update Risk Level? (y/n): ").strip().lower()
    if change_risk == "y":
        asset["Risk Level"] = prompt_choice("Risk Level", RISK_LEVELS)

    change_status = input("Update Security Status? (y/n): ").strip().lower()
    if change_status == "y":
        asset["Security Status"] = prompt_choice("Security Status", SECURITY_STATUSES)

    save_assets(assets)
    print(f"  Asset '{asset['Asset ID']}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = prompt_nonempty("Enter Asset ID to delete")
    for i, a in enumerate(assets):
        if a["Asset ID"].lower() == asset_id.lower():
            confirm = input(f"Are you sure you want to delete '{a['Asset Name']}'? (y/n): ").strip().lower()
            if confirm == "y":
                assets.pop(i)
                save_assets(assets)
                print(f"  Asset '{asset_id}' deleted successfully.")
            else:
                print("  Deletion cancelled.")
            return
    print("  No asset found with that ID.")


def print_asset(a):
    print("-----------------------------------------")
    print(f"Asset ID    : {a['Asset ID']}")
    print(f"Asset Name  : {a['Asset Name']}")
    print(f"Asset Type  : {a['Asset Type']}")
    print(f"IP Address  : {a['IP Address']}")
    print(f"OS          : {a['Operating System']}")
    print(f"Department  : {a['Owner/Department']}")
    print(f"Risk Level  : {a['Risk Level']}")
    print(f"Status      : {a['Security Status']}")


def display_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets found.")
    else:
        for a in assets:
            print_asset(a)
    print("-----------------------------------------")
    print(f"Total Assets      : {len(assets)}")
    print(f"Critical Assets   : {sum(1 for a in assets if a['Risk Level'] == 'Critical')}")
    print(f"High Risk Assets  : {sum(1 for a in assets if a['Risk Level'] == 'High')}")
    print(f"Medium Risk Assets: {sum(1 for a in assets if a['Risk Level'] == 'Medium')}")
    print(f"Low Risk Assets   : {sum(1 for a in assets if a['Risk Level'] == 'Low')}")
    print(f"Vulnerable Assets : {sum(1 for a in assets if a['Security Status'] == 'Vulnerable')}")
    print(f"Warning Assets    : {sum(1 for a in assets if a['Security Status'] == 'Warning')}")
    print(f"Secure Assets     : {sum(1 for a in assets if a['Security Status'] == 'Secure')}")
    print("=========================================")


def seed_sample_data(assets):
    """Load the 3 sample assets from the spec, if the inventory is empty."""
    if assets:
        print("  Inventory is not empty; seeding skipped.")
        return
    sample = [
        {
            "Asset ID": "A101", "Asset Name": "HR-PC-01", "Asset Type": "Workstation",
            "IP Address": "192.168.1.10", "Operating System": "Windows 11",
            "Owner/Department": "HR", "Risk Level": "Medium", "Security Status": "Secure",
        },
        {
            "Asset ID": "A102", "Asset Name": "Web-Server", "Asset Type": "Server",
            "IP Address": "192.168.1.20", "Operating System": "Ubuntu",
            "Owner/Department": "IT", "Risk Level": "Critical", "Security Status": "Vulnerable",
        },
        {
            "Asset ID": "A103", "Asset Name": "Core-Router", "Asset Type": "Router",
            "IP Address": "192.168.1.1", "Operating System": "Cisco IOS",
            "Owner/Department": "Network", "Risk Level": "High", "Security Status": "Warning",
        },
    ]
    assets.extend(sample)
    save_assets(assets)
    print("  Sample data loaded.")


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

def main_menu():
    assets = load_assets()

    menu = """
=========================================
 CYBERSECURITY ASSET INVENTORY SYSTEM
=========================================
1. Add Asset
2. Search Asset
3. Update Asset
4. Delete Asset
5. Display All Assets
6. Load Sample Data
7. Exit
"""
    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            search_asset(assets)
        elif choice == "3":
            update_asset(assets)
        elif choice == "4":
            delete_asset(assets)
        elif choice == "5":
            display_assets(assets)
        elif choice == "6":
            seed_sample_data(assets)
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main_menu()
