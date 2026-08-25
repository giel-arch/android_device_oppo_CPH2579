$(call inherit-product, $(SRC_TARGET_DIR)/product/aosp_arm64.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base.mk)

# Inherit TWRP Core Products
$(call inherit-product, vendor/twrp/config/common.mk)

# Device Identifier
PRODUCT_DEVICE := CPH2579
PRODUCT_NAME := omni_CPH2579
PRODUCT_BRAND := OPPO
PRODUCT_MODEL := Oppo A38
PRODUCT_MANUFACTURER := oppo

PRODUCT_BUILD_VENDOR_BOOT_IMAGE := true
PRODUCT_GMS_CLIENTID_BASE := android-oppo
