cur_frm.cscript.brand_type=function(doc,cdt,cdn)
{
	var brand=doc.brand;
	var brand_type=doc.brand_type;
	frappe.call({
		method:'master.master.doctype.add_rate.add_rate.get_latest_purchase_rate',
		args:{b:brand,bt:brand_type},
		callback:function(r)
		{
			cur_frm.set_value("latest_purchase_rate",r.message)
		}
	})
}