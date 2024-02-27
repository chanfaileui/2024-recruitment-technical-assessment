from dataclasses import dataclass
from collections import Counter

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    parent_ids = set()
    for file in files:
        if file.parent != -1:
            parent_ids.add(file.parent)

    leaves = []
    for file in files:
        if file.id not in parent_ids:
            leaves.append(file)
            
    return [leaf.name for leaf in leaves]

"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    all_categories = []
    for file in files:
        all_categories.extend(file.categories)
    
    all_categories.sort()
    counts = Counter(all_categories)
    return [c[0] for c in counts.most_common(k)]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    def total_size(file):
        total = file.size
        
        for child in files:
            if child.parent == file.id:
                total += total_size(child)
                
        return total
    
    if not files:
        return 0
    
    return max(total_size(file) for file in files)


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
