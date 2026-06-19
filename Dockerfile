# MedSea Site - nginx static server
FROM nginx:alpine

# Copy site files
COPY site/ /usr/share/nginx/html/

# Copy nginx config
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8855

HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -q --spider http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
