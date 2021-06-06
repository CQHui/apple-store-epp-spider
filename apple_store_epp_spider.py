import requests
from bs4 import BeautifulSoup


# for num in range(800000, 899999):
start = 803136
end = 806275
total = 0
for num in range(start, end):
    # if (num - start) * 100 % (end - start) == 0:
    #     print("Processing: " + str((num - start) * 100 // (end - start)) + '%')
    url = 'https://www.apple.com.cn/cn_epp-discounted_' + str(num) + '/shop/open/salespolicies/program_agreement'
    try:
        page = requests.get(url)
    except Exception as e:
        print("error in parsing index:" + str(num))
        continue
    if (page.ok):
        soup = BeautifulSoup(page.text, 'lxml')
        # print(soup)
        script_tags = soup.body.find_all('script')
        for script_tag in script_tags:
            text = script_tag.text
            if 'window.asMetrics.initialize'.lower() in text.lower():
                # print(text)
                try:
                    name = text[text.index('computedCustomStoreName: "AOS: ') + 31:]
                    print(name[0: name.index('\n\n') - 1] + ":" + url)
                    total = total + 1
                except Exception as e:
                    print("error in parsing index:" + str(num))
print("total is " + str(total))



