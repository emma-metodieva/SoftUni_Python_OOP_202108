# L05-02. Class and Static Methods - Exercise
# 01. Photo Album

from math import ceil


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []
        for page in range(pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for p, page in enumerate(self.photos):
            if len(page) < 4:
                self.photos[p].append(label)
                return f"{label} photo added successfully " \
                       f"on page {p + 1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        display = "-----------"
        for page in self.photos:
            display += f"\n{' '.join(['[]' for photo in page])}"
            display += f"\n-----------"
        return display


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
