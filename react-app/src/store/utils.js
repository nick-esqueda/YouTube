export const normalizeOneLevel = (dataArr) => {
    return dataArr.reduce((obj, data) => {
        const dateParts = data.createdAt.split(' ');
        data.createdAt = `${dateParts[2]} ${dateParts[1]}, ${dateParts[3]}`
        obj[data.id] = data;
        return obj;
    }, {})
}
