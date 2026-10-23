from langchain_community.document_loaders import WebBaseLoader

urls = "https://www.apple.com/in/iphone-duo/?afid=p240%7Cgo~cmp-24228438606~adg-200093663197~ad-826554162860_kwd-2500645992655~dev-c~ext-~prd-~mca-~nt-search&cid=wwa-in-kwgo-iphone-noncore_iphoneduo-iphoneduo_general-iphoneduo_hero_preorder_101626-iPhoneDuo-iPhoneDuo_General"

data = WebBaseLoader(urls)

docs = data.load()

print(docs[0].page_content)

