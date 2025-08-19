# Guide

**NOTE: This repo forked from https://github.com/speaches-ai/speaches**

## Prepare buildx
```bash
# 1) Install Docker (...)

# 2) Ensure buildx
docker buildx version

# 3) Regist QEMU/binfmt to support arm64 exec runtime in build
docker run --privileged --rm tonistiigi/binfmt --install arm64

# 4) create buildx builder
docker buildx create --name jetson-builder --use
docker buildx inspect --bootstrap
```

## For latest （Jetpack R36）

**Orin** Only

```bash
# pull
# docker pull nvcr.io/nvidia/l4t-jetpack:r36.4.0 # latest @ 2025-08-14
# build
DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose -f compose.l4t.yaml build
# save
mkdir -p images
docker save speaches:jetson-latest > images/speaches_jetson-latest.tar
```
## For Jetpack R35

**Xavier | Orin**

```bash
# pull
# docker pull nvcr.io/nvidia/l4t-jetpack:r35.4.1 # latest @ 2025-08-14
# build
DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose -f compose.l4t-r35.yaml build
# save
mkdir -p images
docker save speaches:jetson-r35 > images/speaches_jetson-r35.tar
```

## More Previous

Like the TX2 Modules using the older compile toolchain, you can modified the [Dockerfile.l4t](Dockerfile.l4t) like [Dockerfile.l4t-r35](Dockerfile.l4t-r35)

## Note
*CTranslater2:: ctranslate2/src/ops/mean_gpu.cu*

The source code
```c
output[blockIdx.x] /= AccumT(axis_size);
```
is only support on CUDA>=12.0, while JP35 Only have CUDA 11.4, So I have modified this operator to support it.