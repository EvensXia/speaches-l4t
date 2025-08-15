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

## Pull Base Image
```bash
docker pull nvcr.io/nvidia/l4t-jetpack:r36.4.0 # latest @ 2025-08-14
```

## Build
```bash
DOCKER_DEFAULT_PLATFORM=linux/arm64 docker compose -f compose.l4t.yaml build
```

## Store
```bash
mkdir -p images
docker save speaches:jetson-latest > images/speaches_jetson-latest.tar
```