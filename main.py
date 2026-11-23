from phep_tinh import cong, tru, nhan, chia


def main():
    a = 20
    b = 4

    tong = cong(a, b)
    hieu = tru(a, b)
    tich = nhan(a, b)
    thuong = chia(a, b)

    print(f"Tong: {tong}")
    print(f"Hieu: {hieu}")
    print(f"Tich: {tich}")
    print(f"Thuong: {thuong}")
    print("Chuong trinh tinh toan Python")


if __name__ == "__main__":
    main()
