# CSCI 1250 Lab 3: Advanced Challenges
## Email Security Manager - Extended Features

**Prerequisites**: Complete Parts 1-3 of the main lab before attempting these challenges.

This file contains advanced programming challenges for students who finish the main lab early or want to explore more complex applications of functions and sets.

---

# Challenge 1: Complete Email Security Manager (35 minutes)

## Building a Production-Ready Security System

Now we'll combine everything: functions working in sequence AND set operations to build a comprehensive email security manager that could actually be used in a real IT environment.

### Challenge 1A: Email Security Manager
Create a new file: `email_security_manager.py`

```python
def load_domain_categories():
    """Load our email domain security categories"""
    
    # Based on Ryan's actual spam domain list!
    high_risk = {
        "hacknotice.com",
        "cyberdefense.com", 
        "cyberhillpartners.com",
        "cyberpaperpushers-it.com"
    }
    
    medium_risk = {
        "alteryx.com",
        "druva.com",
        "dataappendservice.com", 
        "datadigitalcenter.com",
        "dataitlab.com",
        "datasolutionprovide.com"
    }
    
    marketing_domains = {
        "e.alteryx.com",
        "em.proofpoint.com", 
        "email.box.com",
        "email.emeraldclub.com",
        "email.empower.com"
    }
    
    return high_risk, medium_risk, marketing_domains

def calculate_risk_score(domain, high_risk, medium_risk):
    """Calculate a numeric risk score for a domain"""
    base_score = 0
    
    # Direct matches
    if domain in high_risk:
        base_score += 100
    elif domain in medium_risk:
        base_score += 50
    
    # Pattern analysis
    risk_keywords = ["cyber", "hack", "data", "append", "blast"]
    for keyword in risk_keywords:
        if keyword in domain:
            base_score += 10
    
    # Subdomain analysis
    if domain.startswith("e.") or domain.startswith("email."):
        base_score += 25  # Marketing subdomains
    
    return base_score

def determine_action(risk_score, user_security_level):
    """Decide what action to take based on risk score and user preference"""
    
    if user_security_level == "strict":
        if risk_score >= 25:
            return "BLOCK"
        else:
            return "ALLOW"
    elif user_security_level == "moderate":
        if risk_score >= 50:
            return "BLOCK"
        elif risk_score >= 25:
            return "QUARANTINE"
        else:
            return "ALLOW"
    else:  # relaxed
        if risk_score >= 75:
            return "BLOCK"
        elif risk_score >= 50:
            return "QUARANTINE"
        else:
            return "ALLOW"

def process_email_batch(email_domains, high_risk, medium_risk, security_level):
    """Process multiple email domains and return results"""
    
    results = {
        "blocked": set(),
        "quarantined": set(), 
        "allowed": set()
    }
    
    for domain in email_domains:
        # Calculate risk for this domain
        risk = calculate_risk_score(domain, high_risk, medium_risk)
        
        # Determine action
        action = determine_action(risk, security_level)
        
        # Store result
        if action == "BLOCK":
            results["blocked"].add(domain)
        elif action == "QUARANTINE":
            results["quarantined"].add(domain)
        else:
            results["allowed"].add(domain)
    
    return results

def generate_security_report(results, high_risk, medium_risk):
    """Generate a comprehensive security report"""
    
    print("=" * 50)
    print("EMAIL SECURITY ANALYSIS REPORT")
    print("=" * 50)
    
    # Basic statistics
    total_processed = len(results["blocked"]) + len(results["quarantined"]) + len(results["allowed"])
    blocked_count = len(results["blocked"])
    quarantined_count = len(results["quarantined"])
    allowed_count = len(results["allowed"])
    
    print(f"\n📊 PROCESSING SUMMARY:")
    print(f"   Total emails processed: {total_processed}")
    print(f"   🚫 Blocked: {blocked_count} ({blocked_count/total_processed*100:.1f}%)")
    print(f"   ⚠️  Quarantined: {quarantined_count} ({quarantined_count/total_processed*100:.1f}%)")
    print(f"   ✅ Allowed: {allowed_count} ({allowed_count/total_processed*100:.1f}%)")
    
    # Set analysis
    print(f"\n🔍 THREAT ANALYSIS:")
    
    # Which known threats were caught?
    caught_high_risk = results["blocked"] & high_risk
    caught_medium_risk = results["blocked"] & medium_risk
    
    print(f"   Known high-risk domains blocked: {len(caught_high_risk)}")
    if caught_high_risk:
        print(f"      {sorted(caught_high_risk)}")
    
    print(f"   Known medium-risk domains blocked: {len(caught_medium_risk)}")
    if caught_medium_risk:
        print(f"      {sorted(caught_medium_risk)}")
    
    # Unknown threats (blocked domains not in our lists)
    unknown_blocks = results["blocked"] - (high_risk | medium_risk)
    if unknown_blocks:
        print(f"   🆕 New potential threats discovered: {len(unknown_blocks)}")
        print(f"      {sorted(unknown_blocks)}")

def main():
    """Orchestrate the complete email security analysis"""
    
    print("🔐 Email Security Manager Starting...")
    
    # Step 1: Load our threat intelligence
    high_risk, medium_risk, marketing = load_domain_categories()
    
    # Step 2: Simulate incoming email domains
    incoming_emails = {
        "hacknotice.com",           # Known high risk
        "dataappendservice.com",    # Known medium risk  
        "google.com",               # Clean
        "suspicious-new-domain.ru", # Unknown potential threat
        "email.box.com",            # Marketing
        "etsu.edu",                 # Clean educational
        "cyber-threat-new.net",     # Unknown potential threat
        "druva.com"                 # Known medium risk
    }
    
    print(f"📧 Processing {len(incoming_emails)} incoming emails...")
    
    # Step 3: Get user security preference
    print("\nSecurity Levels:")
    print("  strict   - Block anything suspicious")
    print("  moderate - Balance security and convenience") 
    print("  relaxed  - Only block obvious threats")
    
    security_level = input("Choose security level (strict/moderate/relaxed): ").strip().lower()
    if security_level not in ["strict", "moderate", "relaxed"]:
        security_level = "moderate"
        print("Invalid choice, using 'moderate'")
    
    # Step 4: Process the email batch
    results = process_email_batch(incoming_emails, high_risk, medium_risk, security_level)
    
    # Step 5: Generate comprehensive report
    generate_security_report(results, high_risk, medium_risk)
    
    print(f"\n🎯 Security analysis complete using '{security_level}' settings.")

if __name__ == "__main__":
    main()
```

**Your Task**:
1. Run the program with different security levels and compare the results
2. Add some domains from Ryan's original list to `incoming_emails` and test
3. Modify the `risk_keywords` list and see how it affects scoring

---

# Challenge 2: Smart Blocklist Updater (40 minutes)

## Advanced Set Operations for Threat Intelligence

Design a system that automatically updates your blocklists based on multiple intelligence sources while avoiding false positives.

### Challenge 2A: Advanced Set Operations
Create a new file: `smart_updater.py`

```python
def load_intelligence_sources():
    """Load threat intelligence from multiple sources"""
    
    # Government threat feed
    government_feed = {
        "nation-state.ru", "apt-group.cn", "ransomware-new.onion",
        "dataappendservice.com", "cyberpaperpushers-it.com"
    }
    
    # Commercial threat feed
    commercial_feed = {
        "spam-blast.net", "ad-fraud.biz", "fake-bank.net", 
        "dataappendservice.com", "phishing-kit.org"
    }
    
    # Community reports (might have false positives)
    community_feed = {
        "suspicious-maybe.com", "dataappendservice.com", 
        "user-reported.net", "false-positive.edu"
    }
    
    # Our current trusted blocklist
    current_blocklist = {
        "old-threat.net", "legacy-spam.com", "dataappendservice.com"
    }
    
    # Known false positives (legitimate sites wrongly reported)
    false_positives = {
        "legitimate-business.com", "false-positive.edu", "good-site.org"
    }
    
    return government_feed, commercial_feed, community_feed, current_blocklist, false_positives

def calculate_threat_confidence(domain, gov_feed, commercial_feed, community_feed):
    """Calculate confidence level based on how many sources report the threat"""
    confidence_score = 0
    sources = []
    
    if domain in gov_feed:
        confidence_score += 50
        sources.append("Government")
    
    if domain in commercial_feed:
        confidence_score += 30
        sources.append("Commercial")
    
    if domain in community_feed:
        confidence_score += 20