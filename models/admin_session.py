#!/usr/bin/python3
"""Admin session module for the admin session model"""


class AdminSession:
    """Admin session model"""
    def __init__(self, admin_id, session_id):
        """initializes the admin session"""
        self.admin_id = admin_id
        self.session_id = session_id
        self.expiration = None
    
    def __str__(self):
        """string representation of the admin session"""
        return "Admin Session: {}".format(self.admin_id)
    