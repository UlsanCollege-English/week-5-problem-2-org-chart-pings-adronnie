# src/org_reviewers.py

def count_senior(root, min_level):
    """
    Return how many people in the org tree have level >= min_level.
    Node format: {"name": str, "level": int, "reports": [nodes]}
    """
    # Base case: no root or invalid structure
    if not root or not isinstance(root, dict):
        return 0

    # Get current node's level and reports safely
    level = root.get("level", 0)
    reports = root.get("reports", [])

    # Count this person if they meet or exceed min_level
    count = 1 if level >= min_level else 0

    # Recurse over each report
    for r in reports:
        count += count_senior(r, min_level)

    return count
