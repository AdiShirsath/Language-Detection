# Language Detection Twirp Service

This is a Language detection service. When server receives request from client it will return response. Response will be name of language of the text.

> For ML-model training and other information about data please- [visit](https://github.com/AdiShirsath/Language-Detection)

## How to use:-
1. Make sure you have [GO](https://golang.org/) and [protoc](https://github.com/protocolbuffers/protobuf/releases/latest) compiler is properly setup.
2. Install twirp code generator- `go get -u github.com/verloop/twirpy/protoc-gen-twirpy`
3. Generate code in generated dir using protoc- `protoc --twirpy_out=generated --python_out=generated detection.proto`
4. Once we have all above setup run server.py file.
5. Then run client.py. Can change requested text in this file.


## Demo
![language_detection](https://user-images.githubusercontent.com/75840165/131448104-d3ec0d37-7e3f-4ed6-9528-4d3144527013.gif)
