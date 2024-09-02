- Cloud Control Manager - Cloud Vendor Neutral via externalize integration
    - AWS ESB CSI driver (maintained by AWS)
- AppArmor - Strict Security Rules as a Security Guard by using 'kube-apparmor-manager'
    1. /etc/apparmor.d/custom-profile
        profile custom-profile lags=
        (attach_disconnected, mediate_deleted)
        {
            capabilities:
            /etc/passwd r, # Allows reading
            /etc/shadow w, # Denies writing
        }

    2. sudo apparmor_parser -r -W /etc/apparmor.d/custom-profile

    3. Pod configuration
        ...
        - annotations:
            container.apparmor.security.beta.kubernetes.io/app-container: localhost/custom-profile
        ...

- Debugging via custom debugging profile (such as debug a original image without shell)
    kubectl debug <pod-name> -it --image <image-name> --custom custom-profile.json

- Kube Proxy improvements for externalTrafficPolicy: Cluster
    ToBeDeletedByClusterAutoscaler

- Replicate Pods Scale Down via Random Balancing mode (for example: 3 zones)
