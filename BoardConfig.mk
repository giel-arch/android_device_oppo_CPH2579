DEVICE_PATH := device/oppo/CPH2579

# Target Architecture
TARGET_ARCH := arm64
TARGET_ARCH_VARIANT := armv8-a
TARGET_CPU_ABI := arm64-v8a
TARGET_CPU_ABI2 :=
TARGET_CPU_VARIANT := generic

TARGET_2ND_ARCH := arm
TARGET_2ND_ARCH_VARIANT := armv7-a-neon
TARGET_2ND_CPU_ABI := armeabi-v7a
TARGET_2ND_CPU_ABI2 := armeabi
TARGET_2ND_CPU_VARIANT := generic

# Perbaikan Error "Building a 32-bit-app-only product on a 64-bit device"
TARGET_CPU_ABI_LIST_64_BIT := arm64-v8a
TARGET_CPU_ABI_LIST_32_BIT := armeabi-v7a,armeabi
TARGET_CPU_ABI_LIST := $(TARGET_CPU_ABI_LIST_64_BIT),$(TARGET_CPU_ABI_LIST_32_BIT)

# Bootloader & Platform
TARGET_BOOTLOADER_BOARD_NAME := CPH2579
TARGET_BOARD_PLATFORM := mt6769

# Prebuilt Kernel & DTB Setup
BOARD_KERNEL_CMDLINE := bootconfig loop.max_part=7
BOARD_KERNEL_BASE := 0x40000000
BOARD_KERNEL_PAGESIZE := 2048
TARGET_PREBUILT_KERNEL := $(DEVICE_PATH)/prebuilt/kernel
TARGET_PREBUILT_DTB := $(DEVICE_PATH)/prebuilt/dtb
BOARD_MKBOOTIMG_ARGS := --ramdisk_offset 0x04000000 --tags_offset 0x0E000000 --dtb $(TARGET_PREBUILT_DTB)

# Dynamic Partitions & Fastbootd
BOARD_SUPER_PARTITION_GROUPS := main
BOARD_MAIN_SIZE := 0 # Sesuaikan jika membuat installer super
BOARD_BUILD_SYSTEM_ROOT_IMAGE := false
BOARD_HAS_LARGE_FILESYSTEM := true

# TWRP Specific Flags#
TW_THEME := portrait_hdpi
TW_SCREEN_WIDTH := 720
TW_SCREEN_HEIGHT := 1600
RECOVERY_SDCARD_ON_DATA := true
TW_EXCLUDE_DEFAULT_USB_INIT := true
TW_EXTRA_LANGUAGES := true
TW_INCLUDE_CRYPTO := false
TW_INPUT_BLACKLIST := "hbtp_vm"
TW_USE_TOOLBOX := true
TW_INCLUDE_REPACKTOOLS := true

# ============================================
# TWRP-specific build fixes
# ============================================

# Disable VTS fuzzers (not needed for recovery)
DISABLE_VTS := true

# Allow missing dependencies for TWRP
ALLOW_MISSING_DEPENDENCIES := true

# Skip VTS modules
#PRODUCT_SOONG_NAMESPACES := $(filter-out vts,$(PRODUCT_SOONG_NAMESPACES))
