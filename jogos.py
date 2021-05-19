def findNumber(arr, k):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = int(input("digite um número: "))
    for c in range(len(arr)):
        if k == arr[c]:
            print("sim")
            break
        else:
            print("Não")






if __name__ == '_main_':
    arr_count = int (input().strip())
    arr=[]
    for c in range(arr_count):
        arr_intem = int(input().strip())
        arr.append(arr_intem)
        