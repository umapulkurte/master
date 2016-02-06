# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "master"
app_title = "Master"
app_publisher = "Wayzon"
app_description = "App for master data of hotel"
app_icon = "icon-tasks"
app_color = "blue"
app_email = "info@wayzon.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/master/css/master.css"
# app_include_js = "/assets/master/js/master.js"

# include js, css files in header of web template
# web_include_css = "/assets/master/css/master.css"
# web_include_js = "/assets/master/js/master.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "master.install.before_install"
# after_install = "master.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "master.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"master.tasks.all"
# 	],
# 	"daily": [
# 		"master.tasks.daily"
# 	],
# 	"hourly": [
# 		"master.tasks.hourly"
# 	],
# 	"weekly": [
# 		"master.tasks.weekly"
# 	]
# 	"monthly": [
# 		"master.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "master.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "master.event.get_events"
# }

