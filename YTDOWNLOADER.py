from pytube import YouTube


def get_res_(streams, res):
    stream = list(filter(lambda x:x.resolution, streams))
    return stream

link = input("Enter the link here: ")
res = input("Enter the res here: ")
vid = YouTube(link)

downloadfile = get_res_(vid.streams,res)[0]
downloadfile.download()


