L1 = [10,20,30]
M1 = L1
M2 = [10,20,30]
print(L1 == M1) #True
print(L1 is M1) #True
print(L1 is M2) #False
print(L1 == M2) #True


book_database = [
    {
        # EMPTY DICTIONARY AT INDEX 0
    },

    {
    'bk_title'          :   'Artificial Intelligence A Modern Approach',
    'bk_authors'        :   ['Stuart Russel', 'Peter Norvig'],
    'bk_publication'    :   'Pearson',
    'bk_price'          :   1000.0,
    'bk_nr_pages'       :   1288,
    'bk_edition'        :   4,
    'bk_isbn'           :   '978-93-560-6357-0',
    'bk_reprint'        :   4,
    'bk_genre'          :   'Treatise',
    'bk_lang'           :   ['English'],
    'bk_binding_type'   :   "PAPERBACK",
    'bk_nr_copies'      :   8
    },

    {
    'bk_title': 'Dragon Ball and the Margin Boo',
    'bk_authors': ['Stuart Russel', 'Peter Norvig'],
    'bk_publication': 'Pearson',
    'bk_price': 1000.0,
    'bk_nr_pages': 1288,
    'bk_edition': 4,
    'bk_isbn': '978-93-560-6357-0',
    'bk_reprint': 4,
    'bk_genre': 'Treatise',
    'bk_lang': ['English'],
    'bk_binding_type': "PAPERBACK",
    'bk_nr_copies': 8

    },

    {
        # CONTENT
    },

    {
        # CONTENT
    },


    {
        # CONTENT
    }
]

print(book_database[1]["bk_title"])
print(book_database[1]["bk_isbn"])
print(book_database[2]["bk_title"])
print(book_database[2]["bk_nr_copies"])
print(book_database[3])
