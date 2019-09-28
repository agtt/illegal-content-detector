# Domain Formatter
domain_name = lambda domain: domain.split("//")[-1].split("/")[0].split('?')[0].upper()
domain_format = lambda domain: "WWW." + domain_name(domain) if 'www' not in domain else domain_name(domain)

getclass = lambda service: globals()[service]()

getmethod = lambda serviceclass, method: getattr(serviceclass, method)
