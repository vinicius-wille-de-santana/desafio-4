import requests

def menu():
    verificar= input(str('Você deseja verificar mais alguma URL s/n: ')).lower()
    if verificar == 's':
        main()
    elif verificar == 'n':
        print('programa encerrado ')
        return
    else:
        print("digite uma opção valida ")
        menu()





def main():
    print('Insira abaixo uma URL para verificação, (separados por virgura!)')
    urls = str(input()).lower().split(",")
    http_ativos =[200, 303 ,302 ,404]
    for url in urls:
        url= url.strip()
        if "." not in url:
            print(url,  "Cara , url invalida")
        else:
            if "http" not in url:
                url = f'http://{url}'

            try:
                requisição = requests.get(url)
                if requisição.status_code in http_ativos:
                    print(url," Site Online")
                else:
                    print(url, "Site está Offline ")

            except:
                print(url, (' error'))
    menu()
main()