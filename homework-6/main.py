from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError:
        print("FileNotFoundError: Отсутствует файл item.csv")
    except InstantiateCSVError:
        print(" InstantiateCSVError: Файл item.csv поврежден")
