#!/usr/bin/env python
"""Check Flask URL generation"""
import sys
sys.path.insert(0, 'c:\\Users\\akmau\\Videos\\HealthCareAI-main\\HealthCareAI-Website')

from main import app

with app.app_context():
    print("\n" + "="*70)
    print("FLASK ROUTE ANALYSIS")
    print("="*70)
    
    print("\n[ROUTES REGISTERED]")
    for rule in app.url_map.iter_rules():
        if 'register' in rule.rule or 'login' in rule.rule or 'home' in rule.rule:
            print(f"  {rule.rule:30s} -> {rule.endpoint:20s} | Methods: {rule.methods}")
    
    print("\n[URL GENERATION TEST]")
    print(f"  url_for('home'): {app.config.get('SERVER_NAME', 'localhost')}")
    
    from flask import url_for
    try:
        register_url = url_for('register')
        print(f"  url_for('register'): {register_url}")
    except Exception as e:
        print(f"  url_for('register'): ERROR - {e}")
    
    try:
        login_url = url_for('login')
        print(f"  url_for('login'): {login_url}")
    except Exception as e:
        print(f"  url_for('login'): ERROR - {e}")
    
    try:
        home_url = url_for('home')
        print(f"  url_for('home'): {home_url}")
    except Exception as e:
        print(f"  url_for('home'): ERROR - {e}")

    print("\n" + "="*70 + "\n")
