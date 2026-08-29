$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/base.mk)

# Inherit TWRP Core Products
$(call inherit-product, vendor/twrp/config/common.mk)

# Copy recovery fstab
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/recovery.fstab:$(TARGET_COPY_OUT_RECOVERY)/root/system/etc/recovery.fstab

# Device Identifier
PRODUCT_DEVICE := CPH2579
PRODUCT_NAME := twrp_CPH2579
PRODUCT_BRAND := OPPO
PRODUCT_MODEL := Oppo A38
PRODUCT_MANUFACTURER := oppo

PRODUCT_BUILD_VENDOR_BOOT_IMAGE := true
PRODUCT_GMS_CLIENTID_BASE := android-oppo

# Fix TWRP ramdisk copy error
PRODUCT_COPY_FILES += \
    $(LOCAL_PATH)/task_profiles.json:$(TARGET_COPY_OUT_SYSTEM)/etc/task_profiles.json
