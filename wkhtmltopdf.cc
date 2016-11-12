#include <nan.h>

#ifndef _WIN32
#include <unistd.h>
#endif

using namespace v8;

NAN_MODULE_INIT(Init) {
}

NODE_MODULE(wkhtmltopdf, Init)
