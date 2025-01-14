function l(e) {
                    // var i = n(3646)
                    //   , r = n(6860)
                    //   , a = n(379)
                    //   , s = n(8206);
                    // e.exports = function(e) {
                    //     return i(e) || r(e) || a(e) || s()
                    // }
                }
function i(e) {
                    for (var t = [], n = 0, i = e.length; n < i; n += 2)
                        t.push(parseInt(e.substr(n, 2), 16));
                    return t
                }
function r(e, t) {
                    return e << t | e >>> 32 - t
                }
function a(e) {
                    return (255 & _[e >>> 24 & 255]) << 24 | (255 & _[e >>> 16 & 255]) << 16 | (255 & _[e >>> 8 & 255]) << 8 | 255 & _[255 & e]
                }
function s(e) {
                    return e ^ r(e, 2) ^ r(e, 10) ^ r(e, 18) ^ r(e, 24)
                }
function o(e) {
                    return e ^ r(e, 13) ^ r(e, 23)
                }
function c(e, t, n, r) {
                var c = 3 < arguments.length && void 0 !== r ? r : {}
                  , _ = c.padding
                  , f = void 0 === _ ? "pkcs#5" : _
                  , p = c.mode
                  , _ = c.iv
                  , _ = void 0 === _ ? [] : _
                  , c = c.output
                  , c = void 0 === c ? "string" : c;
                if ("cbc" === p && 16 !== (_ = "string" == typeof _ ? i(_) : _).length)
                    throw new Error("iv is invalid");
                if (16 !== (t = "string" == typeof t ? i(t) : t).length)
                    throw new Error("key is invalid");
                if (e = ("string" == typeof e ? n !== u ? function(e) {
                    for (var t = [], n = 0, i = e.length; n < i; n++) {
                        var r = e.codePointAt(n);
                        if (r <= 127)
                            t.push(r);
                        else if (r <= 2047)
                            t.push(192 | r >>> 6),
                            t.push(128 | 63 & r);
                        else if (r <= 55295 || 57344 <= r && r <= 65535)
                            t.push(224 | r >>> 12),
                            t.push(128 | r >>> 6 & 63),
                            t.push(128 | 63 & r);
                        else {
                            if (!(65536 <= r && r <= 1114111))
                                throw t.push(r),
                                new Error("input is not supported");
                            n++,
                            t.push(240 | r >>> 18 & 28),
                            t.push(128 | r >>> 12 & 63),
                            t.push(128 | r >>> 6 & 63),
                            t.push(128 | 63 & r)
                        }
                    }
                    return t
                }
                : i : l)(e),
                "pkcs#5" === f && n !== u)
                    for (var g = d - e.length % d, m = 0; m < g; m++)
                        e.push(g);
                var b = new Array(32);
                !function(e, t, n) {
                    for (var i = new Array(4), r = new Array(4), s = 0; s < 4; s++)
                        r[0] = 255 & e[0 + 4 * s],
                        r[1] = 255 & e[1 + 4 * s],
                        r[2] = 255 & e[2 + 4 * s],
                        r[3] = 255 & e[3 + 4 * s],
                        i[s] = r[0] << 24 | r[1] << 16 | r[2] << 8 | r[3];
                    i[0] ^= 2746333894,
                    i[1] ^= 1453994832,
                    i[2] ^= 1736282519,
                    i[3] ^= 2993693404;
                    for (var c, l = 0; l < 32; l += 4)
                        c = i[1] ^ i[2] ^ i[3] ^ h[l + 0],
                        t[l + 0] = i[0] ^= o(a(c)),
                        c = i[2] ^ i[3] ^ i[0] ^ h[l + 1],
                        t[l + 1] = i[1] ^= o(a(c)),
                        c = i[3] ^ i[0] ^ i[1] ^ h[l + 2],
                        t[l + 2] = i[2] ^= o(a(c)),
                        c = i[0] ^ i[1] ^ i[2] ^ h[l + 3],
                        t[l + 3] = i[3] ^= o(a(c));
                    if (n === u)
                        for (var d, _ = 0; _ < 16; _++)
                            d = t[_],
                            t[_] = t[31 - _],
                            t[31 - _] = d
                }(t, b, n);
                for (var v = [], y = _, $ = e.length, w = 0; d <= $; ) {
                    var C = e.slice(w, w + 16)
                      , x = new Array(16);
                    if ("cbc" === p)
                        for (var T = 0; T < d; T++)
                            n !== u && (C[T] ^= y[T]);
                    !function(e, t, n) {
                        for (var i = new Array(4), r = new Array(4), o = 0; o < 4; o++)
                            r[0] = 255 & e[4 * o],
                            r[1] = 255 & e[4 * o + 1],
                            r[2] = 255 & e[4 * o + 2],
                            r[3] = 255 & e[4 * o + 3],
                            i[o] = r[0] << 24 | r[1] << 16 | r[2] << 8 | r[3];
                        for (var c, l = 0; l < 32; l += 4)
                            c = i[1] ^ i[2] ^ i[3] ^ n[l + 0],
                            i[0] ^= s(a(c)),
                            c = i[2] ^ i[3] ^ i[0] ^ n[l + 1],
                            i[1] ^= s(a(c)),
                            c = i[3] ^ i[0] ^ i[1] ^ n[l + 2],
                            i[2] ^= s(a(c)),
                            c = i[0] ^ i[1] ^ i[2] ^ n[l + 3],
                            i[3] ^= s(a(c));
                        for (var u = 0; u < 16; u += 4)
                            t[u] = i[3 - u / 4] >>> 24 & 255,
                            t[u + 1] = i[3 - u / 4] >>> 16 & 255,
                            t[u + 2] = i[3 - u / 4] >>> 8 & 255,
                            t[u + 3] = 255 & i[3 - u / 4]
                    }(C, x, b);
                    for (var k = 0; k < d; k++)
                        "cbc" === p && n === u && (x[k] ^= y[k]),
                        v[w + k] = x[k];
                    "cbc" === p && (y = n !== u ? x : C),
                    $ -= d,
                    w += d
                }
                return "pkcs#5" === f && n === u && (f = v[v.length - 1],
                v.splice(v.length - f, f)),
                "array" !== c ? n !== u ? v.map(function(e) {
                    return 1 === (e = e.toString(16)).length ? "0" + e : e
                }).join("") : function(e) {
                    for (var t = [], n = 0, i = e.length; n < i; n++)
                        240 <= e[n] && e[n] <= 247 ? (t.push(String.fromCodePoint(((7 & e[n]) << 18) + ((63 & e[n + 1]) << 12) + ((63 & e[n + 2]) << 6) + (63 & e[n + 3]))),
                        n += 3) : 224 <= e[n] && e[n] <= 239 ? (t.push(String.fromCodePoint(((15 & e[n]) << 12) + ((63 & e[n + 1]) << 6) + (63 & e[n + 2]))),
                        n += 2) : 192 <= e[n] && e[n] <= 223 ? (t.push(String.fromCodePoint(((31 & e[n]) << 6) + (63 & e[n + 1]))),
                        n++) : t.push(String.fromCodePoint(e[n]));
                    return t.join("")
                }(v) : v
            }
function sm4Encrypt(e) {
        return c(e, _sm4pubkey, 1)
    }

const jsonString = process.argv[2];
//var jsonString = '{"pd":"godlike_wyds_xcx","pkid":"VYoLaWc","pkht":"ds.163.com","channel":102,"id":"79F99E134C55AD10DDB46E9A9C98BAAFC08E2790D34B1CC7BE360B76800E13A54DA82975177DD53F2BE536734B003B1176182B1CE9404C019E5382753F21E98068FC008E16E2FFAAECFA39868F9C639C140C5D0EE0985303D2DD0BF4A83856AE93901AF134F5CAFC94AE5B5C99F7EE6C","cap":"CN31_q9ezSKGx_2qF0YAbqfd1_CfyaQHsvIB_mXHQ.ggBpTX0T41ndl6DxdhKEPboz7XC1KAntQZJqbfSliOUecRx4G1hkkb44S.TqJ4SkFZBM9wZy6VJu9bSr01JIprgUnYvOh.6oVbjdY8b8xorRJeiR8SRJX8cyuBhWp0DzchYUVIYEKAf15-L1r.BKNx_bWaF40Z7BihpC6ok_-55UxGB.ns7PGPUxkl8E_HhSojw0SzLVgdokM-9Du5.JX.igH0I","un":"13122546736"}'
var _sm4pubkey = "BC60B8B9E4FFEFFA219E5AD77F11F9E2";
var u = 0
    , d = 16
    , _ = [214, 144, 233, 254, 204, 225, 61, 183, 22, 182, 20, 194, 40, 251, 44, 5, 43, 103, 154, 118, 42, 190, 4, 195, 170, 68, 19, 38, 73, 134, 6, 153, 156, 66, 80, 244, 145, 239, 152, 122, 51, 84, 11, 67, 237, 207, 172, 98, 228, 179, 28, 169, 201, 8, 232, 149, 128, 223, 148, 250, 117, 143, 63, 166, 71, 7, 167, 252, 243, 115, 23, 186, 131, 89, 60, 25, 230, 133, 79, 168, 104, 107, 129, 178, 113, 100, 218, 139, 248, 235, 15, 75, 112, 86, 157, 53, 30, 36, 14, 94, 99, 88, 209, 162, 37, 34, 124, 59, 1, 33, 120, 135, 212, 0, 70, 87, 159, 211, 39, 82, 76, 54, 2, 231, 160, 196, 200, 158, 234, 191, 138, 210, 64, 199, 56, 181, 163, 247, 242, 206, 249, 97, 21, 161, 224, 174, 93, 164, 155, 52, 26, 85, 173, 147, 50, 48, 245, 140, 177, 227, 29, 246, 226, 46, 130, 102, 202, 96, 192, 41, 35, 171, 13, 83, 78, 111, 213, 219, 55, 69, 222, 253, 142, 47, 3, 255, 106, 114, 109, 108, 91, 81, 141, 27, 175, 146, 187, 221, 188, 127, 17, 217, 92, 65, 31, 16, 90, 216, 10, 193, 49, 136, 165, 205, 123, 189, 45, 116, 208, 18, 184, 229, 180, 176, 137, 105, 151, 74, 12, 150, 119, 126, 101, 185, 241, 9, 197, 110, 198, 132, 24, 240, 125, 236, 58, 220, 77, 32, 121, 238, 95, 62, 215, 203, 57, 72]
    , h = [462357, 472066609, 943670861, 1415275113, 1886879365, 2358483617, 2830087869, 3301692121, 3773296373, 4228057617, 404694573, 876298825, 1347903077, 1819507329, 2291111581, 2762715833, 3234320085, 3705924337, 4177462797, 337322537, 808926789, 1280531041, 1752135293, 2223739545, 2695343797, 3166948049, 3638552301, 4110090761, 269950501, 741554753, 1213159005, 1684763257];
const result = sm4Encrypt(jsonString);
console.log(result)
