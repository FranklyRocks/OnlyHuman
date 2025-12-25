#!/usr/bin/env python3

with open('rawlist.txt', 'r') as f:
    domains = [line.strip() for line in f if line.strip()]

with open('list.txt', 'w') as f:
    f.write('# Block websites\n')
    for domain in domains:
        f.write(f'||{domain}^$doc\n')
    
    f.write('\n# Block Google results\n')
    for domain in domains:
        f.write(f'google.com##a[href*="{domain}"]:upward(2):remove()\n')
    
    f.write('\n# Block Bing results\n')
    for domain in domains:
        f.write(f'www.bing.com##li.b_algo:has(a[aria-label="{domain}"])\n')
    
    f.write('\n# Block DuckDuckGo results\n')
    for domain in domains:
        f.write(f'duckduckgo.com##a[href*="{domain}"]:upward(4):remove()\n')
    
    f.write('\n# Block Yandex results\n')
    for domain in domains:
        f.write(f'yandex.com###search-result > li:has(a[href*="{domain}"])\n')
    
    f.write('\n# Block Ecosia results\n')
    for domain in domains:
        f.write(f'ecosia.org##.result__body:has(a[href*="{domain}"])\n')
