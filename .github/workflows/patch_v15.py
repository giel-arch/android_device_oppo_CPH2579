import sys

try:
    content = open('bootable/recovery/minuitwrp/graphics_drm.cpp').read()
    
    # 1. We replace drm_init completely!
    old_init_start = "GRSurface* drm_init(minui_backend* backend __unused) {"
    old_init_end = "return draw_buf;\n}"
    
    # Find the block
    start_idx = content.find(old_init_start)
    end_idx = content.find(old_init_end, start_idx) + len(old_init_end)
    
    if start_idx == -1 or end_idx < len(old_init_end):
        print("Failed to find drm_init!")
        sys.exit(1)
        
    old_init = content[start_idx:end_idx]
    
    new_init = '''GRSurface* drm_init(minui_backend* backend __unused) {
    printf("V15: Initializing Zero-State-Change Framebuffer Hijack...\\n");
    drm_fd = get_drm_device();
    if (drm_fd < 0) return nullptr;

    drmModeRes* res = drmModeGetResources(drm_fd);
    if (!res) return nullptr;

    uint32_t active_fb_id = 0;
    
    // Attempt 1: Check CRTCs (Legacy)
    for (int i = 0; i < res->count_crtcs; i++) {
        drmModeCrtc* crtc = drmModeGetCrtc(drm_fd, res->crtcs[i]);
        if (crtc && crtc->buffer_id != 0) {
            active_fb_id = crtc->buffer_id;
            drmModeFreeCrtc(crtc);
            break;
        }
        if (crtc) drmModeFreeCrtc(crtc);
    }

    // Attempt 2: Check Planes (Atomic)
    if (active_fb_id == 0) {
        drmModePlaneRes* pres = drmModeGetPlaneResources(drm_fd);
        if (pres) {
            for (uint32_t i = 0; i < pres->count_planes; i++) {
                drmModePlane* plane = drmModeGetPlane(drm_fd, pres->planes[i]);
                if (plane && plane->crtc_id != 0 && plane->fb_id != 0) {
                    active_fb_id = plane->fb_id;
                    drmModeFreePlane(plane);
                    break;
                }
                if (plane) drmModeFreePlane(plane);
            }
            drmModeFreePlaneResources(pres);
        }
    }

    if (active_fb_id == 0) {
        printf("V15: CRITICAL ERROR! No active FB found! Cannot hijack.\\n");
        return nullptr;
    }

    drmModeFB* fb = drmModeGetFB(drm_fd, active_fb_id);
    if (!fb) return nullptr;

    printf("V15: Found Bootloader FB: %dx%d, pitch=%d, handle=%d\\n", fb->width, fb->height, fb->pitch, fb->handle);

    struct drm_mode_map_dumb mreq;
    memset(&mreq, 0, sizeof(mreq));
    mreq.handle = fb->handle;

    if (drmIoctl(drm_fd, DRM_IOCTL_MODE_MAP_DUMB, &mreq) != 0) {
        printf("V15: Failed to map dumb buffer!\\n");
        return nullptr;
    }

    void* ptr = mmap(0, fb->height * fb->pitch, PROT_READ | PROT_WRITE, MAP_SHARED, drm_fd, mreq.offset);
    if (ptr == MAP_FAILED) {
        printf("V15: mmap failed!\\n");
        return nullptr;
    }

    drmModeFreeFB(fb);
    drmModeFreeResources(res);

    // Create hijack surface
    drm_surfaces[1] = (GRSurfaceDrm*)malloc(sizeof(GRSurfaceDrm));
    memset(drm_surfaces[1], 0, sizeof(GRSurfaceDrm));
    drm_surfaces[1]->base.width = fb->width;
    drm_surfaces[1]->base.height = fb->height;
    drm_surfaces[1]->base.row_bytes = fb->pitch;
    drm_surfaces[1]->base.pixel_bytes = 4; // Assuming 32-bit
    drm_surfaces[1]->base.format = PIXEL_FORMAT_RGBA_8888;
    drm_surfaces[1]->base.data = (unsigned char*)ptr;

    draw_buf = (GRSurface*)malloc(sizeof(GRSurface));
    memcpy(draw_buf, &drm_surfaces[1]->base, sizeof(GRSurface));
    draw_buf->data = (unsigned char*)calloc(draw_buf->height * draw_buf->row_bytes, 1);

    printf("V15: Hijack Successful! Bypass complete.\\n");
    return draw_buf;
}'''
    
    content = content.replace(old_init, new_init)
    
    open('bootable/recovery/minuitwrp/graphics_drm.cpp', 'w').write(content)
    print('DRM Direct Memory Write V15 (Zero-State-Change Hijack) applied successfully!')
except Exception as e:
    print('Patching drm_init failed:', e)
