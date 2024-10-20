# TODO Найдите количество книг, которое можно разместить на дискете

disk_size_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

memory_of_one_book_bytes = bytes_per_char * chars_per_line * lines_per_page * pages_per_book

memory_of_one_book_megabytes = memory_of_one_book_bytes / (1024 * 1024)

count = disk_size_mb // memory_of_one_book_megabytes

print("Количество книг, помещающихся на дискету:", int(count))
