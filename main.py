from include.pyside6Import import *
from include.classImport import *


# -------------------- Run App --------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    adm = Admin()
    data = [
        Room("Physics Lab", "A101", "Experiments and equipment", "#AA4444"),
        Room("Computer Room", "B202", "Coding and projects", "#4488AA"),
        Room("Art Studio", "C303", "Creative workspace", "#44AA88"),
        Room("Math Room", "D404", "Problem solving zone", "#AA8844"),
        Room("Chemistry Lab", "E505", "Chemical experiments", "#8844AA"),
        Room("Biology Lab", "F606", "Microscopes and specimens", "#44AA44"),
        Room("Library", "G707", "Books and study area", "#AAAA44"),
        Room("Music Room", "H808", "Instruments and practice", "#44AAAA"),
    ]
    window = Home(data, "Mr. Name Sur")
    window.resize(900, 600)
    window.show()

    sys.exit(app.exec())