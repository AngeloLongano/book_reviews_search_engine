from utils.ManageReviewIndex import MangeReviewIndex



index_manager = MangeReviewIndex()

index_manager.initialize_index()

index_manager.search_index('title:"must read"',"text")
print("------CORREZIONE QUERY-------\n")
index_manager.suggest_words("bool")

