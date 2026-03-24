from gql import gql

GET_ALL_BAOMING_RECORDS_QUERY = gql("""
query getAllBaomingRecords($uid: String, $limit: String) {
  baomings(userId: $uid, sort: "-createdAt", limit: $limit) {
    _id
    tongjiId
    no
    noLabel
    tongjiIdObject {
      _id
      title
      isRepeat
      fixedNo
      isRemove
      noName
    }
    infoKey
    infoVal
  }
}
""")

CREATE_BAOMING_QUERY = gql("""
mutation createBaomingByInput($input: createBaomingInput!) {
  createBaomingByInput(input: $input) {
    _id
  }
}
""")

GET_TONGJI_QUERY = gql("""
query getTongji($_id: String) {
  tongji(_id: $_id) {
    locationInfos {
      name
      latitude
      longtitude
    }
    allowRejctBaoming
    isAnonymous
    isPreFill
    nameListInRowCount
    allowBukaRange
    submitSuccessText
    isHideNameList
    _id
    files
    filesInfos {
      type
      title
      link
    }
    isOpenRanking
    allowManagerChangeResult
    needSignature
    isEvent
    title
    content
    allowBaomingCount
    userAllowBaomingCount
    hasReadMsg
    lastReadTime
    needSubmitLocation
    openLocationInfo
    groupLabelName
    count
    noName
    nameLabel
    needWifi
    wifiInfos {
      ssid
      bssid
    }
    needInfo
    needNotify
    payCount
    needPay
    infoFields
    doneNos
    groupId
    publishResult
    generateQrCode
    showNameList
    hideNameListNo
    allowMultipleBirths
    multipleBirthsGroups {
      title
      nameList {
        groupName
        name
        no
        noLabel
      }
    }
    needLocation
    locations {
      name
      longtitude
      latitude
      distance
    }
    allowSubmitTimeRules {
      _id
      startTime
      endTime
      notifyTime
      notifyTitle
    }
    repeatDaysType
    repeatDays
    repeatDates
    repeatEndDate
    repeatStartDate
    dayRepeatCount
    allowBuka
    isRepeat
    createdAt
    createdBy
    openGids
    removeNos
    restrictGroupMember
    isClosed
    isPassSecurity
    needTimeLimit
    startTime
    endTime
    needImages
    imageIsRequired
    needVideo
    videoIsRequired
    needAudio
    audioIsRequired
    videos
    videoArr
    videoBucket
    requiredFields
    needOptions
    optionFields {
      title
      isImage
      isMulti
      required
      maxSelect
      options
    }
    protectYoung
    isNewForm
    infoForms {
      id
      isRemove
      type
      title
      desc
      descImage
      order
      required
      options
      maxSelect
      minSelect
      mediaSourceType
      textareaRow
      limitCharGt
      limitCharlt
      watermarkInfo
      fullScore
      isInfoOption
      infoOptions {
        title
        isImage
        imageUrl
        score
      }
      restrictPhoto {
        isRestrict
        photoWidth
        photoHeight
        photoSizeMax
        photoSizeMin
        photoType
      }
      fileTypes
      isSignFile
      signFile {
        type
        url
        thumbDatas
      }
      signPosition {
        pageNo
        type
        x
        y
        offsetX
        offsetY
        textVal
        zoomRate
      }
      isScoreOption
      questionOptions {
        title
      }
      showConditions {
        optionId
        optionIdxs
        optionLogic
      }
      showConditionsLogic
      skipToFormId
      allowOther
      optionMaxSelect
      optionIsDropDown
      optionsSettings {
        id
        optionMaxSelect
      }
      isOriginal
      isDownloadOriginal
      banUpdate
      privateResult
      groupInfoForms {
        id
        isRemove
        type
        title
        desc
        order
        required
        options
        maxSelect
        minSelect
        mediaSourceType
        textareaRow
        limitCharGt
        limitCharlt
        allowOther
        isOriginal
        isDownloadOriginal
        banUpdate
        privateResult
        watermarkInfo
        collectAddressType
      }
      collectAddressType
      courseSetting {
        id
        title
        description
        image
        schedule {
          dayOfWeek
          startTime
          endTime
        }
        teacher
        quota
        location
        order
        price
      }
      isGlobalDisplay
    }
    closeQa
    banUpdateAfterDeadline
    canUpdateDuration
    canBookTimeSetting {
      limitSelect
      expiredHidden
      timeShowMode
      bookEndRuleMode
      bookEndRule
      cancelEndRuleMode
      cancelEndRule
    }
    bookProjectInfo {
      title
      desc
      photo
    }
    bookProjectSetting {
      title
      limitPerson
      limitOptionCount
      isRequired
    }
    visitCount
    needCorrectsMode
    baomingCommentPermission
    intros {
      type
      title
      link
      entity
      entityId
      subtitle
      button
      appId
      content
    }
    fillInLicensee
    infoFormsDisplayPosition
    lastUpdateInfoFormsTime
    authorizeInfoFormsRecords {
      submitDayStr
      submitDayIndex
      infoForms {
        id
        isRemove
        type
        title
        desc
        descImage
        order
        required
        options
        maxSelect
        minSelect
        mediaSourceType
        textareaRow
        limitCharGt
        limitCharlt
        watermarkInfo
        fullScore
        isInfoOption
        infoOptions {
          title
          isImage
          imageUrl
          score
        }
        isScoreOption
        questionOptions {
          title
        }
        showConditions {
          optionId
          optionIdxs
          optionLogic
        }
        showConditionsLogic
        skipToFormId
        allowOther
        optionMaxSelect
        optionIsDropDown
        optionsSettings {
          id
          optionMaxSelect
        }
        isOriginal
        isDownloadOriginal
        banUpdate
        privateResult
        groupInfoForms {
          id
          isRemove
          type
          title
          desc
          order
          required
          options
          maxSelect
          minSelect
          mediaSourceType
          textareaRow
          limitCharGt
          limitCharlt
          allowOther
          isOriginal
          isDownloadOriginal
          banUpdate
          privateResult
          watermarkInfo
          collectAddressType
        }
        collectAddressType
        courseSetting {
          id
          title
          description
          image
          schedule {
            dayOfWeek
            startTime
            endTime
          }
          teacher
          quota
          location
          price
          order
        }
      }
    }
    needExamMode
    banViewExamResult
    examDuration
    examForms {
      id
      type
      title
      desc
      limitCharGt
      limitCharlt
      textareaRow
      order
      options
      isTrueFalseOption
      isInfoOption
      infoOptions {
        title
        isImage
        imageUrl
        isVideo
        videoUrl
        score
      }
      answer
      fullScore
      answerAnalysis
      answerAnalysisImages
      scoringRule
      partScore
      allowImageAnwser
      multiTitles {
        title
        answer
        fullScore
      }
    }
    examFullScore
    needNameListQRCode
    qrcodeObj {
      qrcodeSize
      qrcodeStyle
    }
    products
    productsObjects {
      _id
      isOffLine
      title
      pictures
      desc
      promise
      price
      fakePrice
      remainCount
      initRemainCount
      lastCountDay
      tags {
        name
        subTags
      }
      skus {
        name
        tags
        price
        fakePrice
        remain
        initRemainCount
        photo
      }
    }
  }
}
""")
