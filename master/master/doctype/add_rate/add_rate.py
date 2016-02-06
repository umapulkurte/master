# Copyright (c) 2013, Wayzon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AddRate(Document):
	def validate(self):
		b=self.brand;
		bt=self.brand_type;
		r=self.rate;
		q=frappe.db.sql("""select brand,brand_type from `tabAdd Rate` where brand=%s and brand_type=%s""",(b,bt))
		if q:
			q1=frappe.db.sql("""update `tabAdd Rate` set rate=%s where brand=%s and brand_type=%s""",(r,b,bt))
	def before_insert(self):
		b=self.brand;
		bt=self.brand_type;
		q=frappe.db.sql("""select brand,brand_type from `tabAdd Rate` where brand=%s and brand_type=%s""",(b,bt))
		if q:
			frappe.throw("Entry already exists for selected Brand,brandtype")
@frappe.whitelist()
def get_latest_purchase_rate(b,bt):
	q=frappe.db.sql("""select p.date,pi.brand,pi.brand_name,pi.brand_type,pi.type_name,pi.rate 
		from `tabPurchaseinfo` pi,`tabPurchase` p  
		where p.name=pi.parent and pi.brand=%s and pi.brand_type=%s 
		order by date desc limit 1""",(b,bt))
	if q:
		r=q[0][5]
	else:
		frappe.msgprint("Selected Brand,brandtype are not purchased tll now")
		r=0
	return(r)