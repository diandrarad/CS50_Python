filename = input("Filename: ").strip().lower()

ext = filename.rpartition(".")[2]

match ext:
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "zip":
        print("application/zip")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")