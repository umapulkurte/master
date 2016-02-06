from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Add Brand",
					#"description": _("Assign tables to waiters.")
				},
				{
					"type": "doctype",
					"name": "Add Brand Type",
					#"description": _("Generate order table wise")
				},
				{
					"type": "doctype",
					"name": "Add Party",
					#"description": _("Purchase Item")
				},
				{
					"type": "doctype",
					"name": "Table",
					#"description": _("Loose Bottels.")
				},
				{
					"type": "doctype",
					"name": "Waiter",
					#"description": _("Details of each Order id.")
				},
				{
					"type": "doctype",
					"name": "Add Rate",
					#"description": _("For Saving Stock at the end of day")
				},
			]
		}
]